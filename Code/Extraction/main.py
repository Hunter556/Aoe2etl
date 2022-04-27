from unicodedata import name
import src.extract as ex
from src.utils import authentification as auth


def extract(request):
    timestamp = '1596775000'
    api_response = ex.extract_data_from_api('1',
                                         '1596775000')
    bucket_name = 'aoe2spark'
    gcs_key_path = 'data/gcs_aoe2.json'
    client = auth.authentificate_gcs(gcs_key_path)
    ex.upload_results_to_gcs(timestamp=timestamp,
                          api_response=api_response,
                          bucket_name=bucket_name,
                          client=client)
