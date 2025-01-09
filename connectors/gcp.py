# Links
#https://cloud.google.com/docs/authentication/
from google.auth import credentials
from google.oauth2 import service_account
#from google.cloud import storage

def gcp_authenticate()->credentials:
    # Path to your service account key file
    key_path = ''

    # Authenticate using the service account
    credentials = service_account.Credentials.from_service_account_file(key_path)
    return credentials

