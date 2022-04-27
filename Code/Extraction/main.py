import src.extract as ex
from datetime import datetime, timedelta
from src.utils import authentification as auth
from src.utils import common as cm
import os



def extract(request):
    
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    yesterday = datetime.strftime(yesterday, "%Y-%m-%d")
    timestamp = int(datetime.strptime(yesterday, "%Y-%m-%d").timestamp())
    timestamp = str(timestamp)
    config_filename = 'config_extract.json'
    path_to_file_gcs = os.path.join('config/',config_filename)
    path_to_file_local = os.path.join('config',config_filename)
    bucket_name = 'aoe2spark'
    gcs_key_path = 'data/gcs_aoe2.json'

    client = auth.authentificate_gcs(gcs_key_path)

    cm.download_file_from_gcs(path_to_file_gcs,
                              bucket_name,
                              blob_name=path_to_file_gcs,
                              storage_client=client)

    config_file = cm.read_json(path_to_file_local)
    count = config_file['count']
    api_response = ex.extract_data_from_api(count,
                                         timestamp)


    ex.store_results(timestamp=timestamp,
                          api_response=api_response,
                          bucket_name=bucket_name,
                          client=client)

extract("")