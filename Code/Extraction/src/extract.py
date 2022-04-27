import requests as r
import json
from google.cloud import storage



def extract_data_from_api(count: str, timestamp:str) -> dict :
    request = f'https://aoe2.net/api/matches?game=aoe2de&count={count}&since={timestamp}'
    response = r.get(request)
    return response.json()


def upload_to_bucket(blob_name:str, output:str, bucket_name:str, storage_client:str):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data=output, content_type='application/json')


def upload_results_to_gcs(timestamp:str, api_response:list,  bucket_name:str, client:str):
    print(type(client))
    blob_name = timestamp
    upload_to_bucket(blob_name, json.dumps(api_response), bucket_name, client)