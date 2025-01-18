import datetime as datetime
# Links
#https://cloud.google.com/docs/authentication/
from google.auth import credentials
from google.oauth2 import service_account
#from google.cloud import storage

def gcp_authenticate_withkeyfile(keyfile_name)->credentials:
    # Path to your service account key file
    # Authenticate using the service account file
    try:
        credentials = service_account.Credentials.from_service_account_file(keyfile_name)
    except Exception as e:
        print("Exception in GCP Authentication")
    finally:
        return credentials

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Connection to GCP started at {datetime.now()}")
    start_datetime = datetime.now()
    # Local Variables
    keyfile_path =''
    credentials = gcp_authenticate_withkeyfile(keyfile_path)
    print(f"Connection to GCP at {datetime.now()}")
