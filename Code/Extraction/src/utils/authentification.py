from google.oauth2 import service_account
from google.cloud import storage

def authentificate_gcs(keypath:str):
    """_summary_

    Args:
        keypath (str): _description_

    Returns:
        _type_: _description_
    """    
    credentials = service_account.Credentials.from_service_account_file(
        keypath, scopes=["https://www.googleapis.com/auth/cloud-platform"])

    client = storage.Client(credentials=credentials)
    return client