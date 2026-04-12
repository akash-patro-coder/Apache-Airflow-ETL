from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

# Custom Operator (plugin)
from plugins.custom_operator import PolygonAPIToXComOperator

# Reusable logic (include)
from include.utils.transform import transform_market_data
from include.config import API_KEY, TICKER

# DB Hook (keep if you still want SQLite backup - optional)
from airflow.providers.sqlite.hooks.sqlite import SqliteHook

# GCP
from include.gcp.gcs_upload import upload_to_gcs
from include.gcp.bigquery_load import load_json_from_gcs_to_bq


# Default args
default_args = {
    "retries": 3,
    "retry_delay": timedelta(minutes=5)
}


# DAG Definition
with DAG(
    dag_id="market_etl",
    start_date=datetime(2024, 1, 1, 9),
    schedule="@daily",
    catchup=False,
    max_active_runs=1,
    default_args=default_args,
    tags=["etl", "market", "polygon"]
) as dag:

    # -------------------------
    # 1. EXTRACT
    # -------------------------
    extract_task = PolygonAPIToXComOperator(
        task_id="extract_market_data",
        api_key=API_KEY,
        ticker=TICKER
    )

    # -------------------------
    # 2. TRANSFORM
    # -------------------------
    @task()
    def transform_task(polygon_data, **context):
        ds = context.get("ds")
        return transform_market_data(polygon_data, ds)

    transformed_data = transform_task(extract_task.output)

    # -------------------------
    # 3. LOAD TO SQLITE (optional - keep or remove)
    # -------------------------
    @task()
    def load_task(df):
        hook = SqliteHook("market_database_conn")
        engine = hook.get_sqlalchemy_engine()

        df.to_sql(
            name="market_data",
            con=engine,
            if_exists="append",
            index=False
        )

    sqlite_loaded = load_task(transformed_data)

    # -------------------------
    # 4. UPLOAD TO GCS
    # -------------------------
    @task()
    def upload_to_gcs_task(df):
        data = df.to_dict(orient="records")

        bucket_name = "market-data-bucket-prod"
        file_name = f"market_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

        upload_to_gcs(bucket_name, file_name, data)

        return file_name

    gcs_file = upload_to_gcs_task(transformed_data)

    # -------------------------
    # 5. LOAD TO BIGQUERY
    # -------------------------
    @task()
    def load_to_bq_task(file_name):
        project_id = "market-analytics-183"
        dataset_id = "stock_market_dw"
        table_id = "daily_prices"

        gcs_uri = f"gs://market-data-bucket-prod/{file_name}"

        load_json_from_gcs_to_bq(project_id, dataset_id, table_id, gcs_uri)

    bq_loaded = load_to_bq_task(gcs_file)

    # -------------------------
    # DAG FLOW
    # -------------------------
    extract_task >> transformed_data >> sqlite_loaded >> gcs_file >> bq_loaded