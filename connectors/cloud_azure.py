# https://pypi.org/search/?q=azure
# https://pypi.org/project/azure/
# https://azure.github.io/azure-sdk/releases/latest/all/python.html
# https://learn.microsoft.com/en-us/azure/developer/python/

from datetime import time, datetime

# Main Program
def azure_authenticate_withkeyfile(keyfile_name):
    # Path to your service account key file
    # Authenticate using the service account file
    try:
        print("")
    except Exception as e:
        print("Exception in Azure Authentication")
    finally:
        print("")

def azure_authenticate_withtoken(token, attribute1, attribute2):
    # Path to your service account key file
    # Authenticate using the service account file
    try:
        print("")
    except Exception as e:
        print("Exception in Azure Authentication")
    finally:
        print("")

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Connection to Azure started at {datetime.now()}")
    start_datetime = datetime.now()
    # Local Variables
    keyfile_path =''
    credentials = azure_authenticate_withkeyfile(keyfile_path)
    print(f"Connection to Azure at {datetime.now()}")