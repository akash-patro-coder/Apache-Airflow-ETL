from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

# Custom Operator (plugin)
from plugins.custom_operator import PolygonAPIToXComOperator

# Reusable logic (include)
from include.utils.transform import transform_market_data
from include.config import API_KEY, TICKER

# DB Hook
from airflow.providers.sqlite.hooks.sqlite import SqliteHook


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
    # 1. EXTRACT (Custom Operator)
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
    # 3. LOAD
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

    load_task(transformed_data)


# -------------------------
# DAG FLOW (visual)
# extract → transform → load
# -------------------------