from google.oauth2 import service_account
from google.cloud import storage

def authentificate_gcs(keypath:str):
    credentials = service_account.Credentials.from_service_account_file(
        keypath, scopes=["https://www.googleapis.com/auth/cloud-platform"])

    client = storage.Client(credentials=credentials)
    return client