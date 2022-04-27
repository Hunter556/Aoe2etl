import json
from google.cloud import storage

def download_file_from_gcs(destination:str, bucket_name:str, blob_name:str, storage_client:str):
    bucket = storage_client.get_bucket(bucket_name)
    # Create a blob object from the filepath
    blob = bucket.blob(blob_name)
    # Download the file to a destination
    blob.download_to_filename(destination)

def read_json(filename):
    with open(f'{filename}', 'r') as f:
        return json.load(f)