from google.cloud import bigquery

def load_json_from_gcs_to_bq(project_id, dataset_id, table_id, gcs_uri):
    """
    Load JSON data from GCS into BigQuery
    """
    client = bigquery.Client(project=project_id)

    table_ref = f"{project_id}.{dataset_id}.{table_id}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,
        write_disposition="WRITE_APPEND"
    )

    load_job = client.load_table_from_uri(
        gcs_uri,
        table_ref,
        job_config=job_config
    )

    load_job.result()  # Wait for job

    print(f"Loaded data into BigQuery: {table_ref}")