from google.cloud import storage
import json
import os

def upload_to_gcs(bucket_name, destination_blob_name, data):
    """
    Upload JSON data to GCS
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Convert data to JSON string
    json_data = json.dumps(data)

    blob.upload_from_string(json_data, content_type="application/json")

    print(f"Uploaded to GCS: {destination_blob_name}")