import requests
import datetime
import os

def connect_to_endpoint(url_value)->str:
    response = ""
    try:
        response = requests.get(url_value)
        if response.status_code == 200:
            print(response.json())
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        #print(f"Failed to retrieve data: {response.status_code}")
    finally:
        return response

if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
