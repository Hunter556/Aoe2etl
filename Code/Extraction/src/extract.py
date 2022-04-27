import requests as r
import json
from google.cloud import storage



def extract_data_from_api(count: str, timestamp:str) -> list :
    """
    
        Extract data from aoe2.net api.

    Args:
        count (str): Number of records to retrieve
        timestamp (str): timestamp

    Returns:
        list: returns api response
    """    
    request = f'https://aoe2.net/api/matches?game=aoe2de&count={count}&since={timestamp}'
    response = r.get(request)
    return response.json()


def upload_to_bucket(blob_name:str, output:str, bucket_name:str, storage_client:str):
    """
        upload json string to gcs bucket as a json file

    Args:
        blob_name (str): name of the blob
        output (str): data
        bucket_name (str): name of the bucket
        storage_client (str): gcs client
    """    
    bucket = storage_client.get_bucket(bucket_name)

    blob = bucket.blob(blob_name)
    blob.upload_from_string(data=output, content_type='application/json')


def store_results(timestamp:str, api_response:list,  bucket_name:str, client:str):
    """
        store resutls into gcs bucket

    Args:
        timestamp (str): timestamp
        api_response (list): api response
        bucket_name (str): name of the bucket
        client (str): gcs client
    """    
    blob_name = timestamp
    upload_to_bucket(blob_name, json.dumps(api_response, indent=4), bucket_name, client)