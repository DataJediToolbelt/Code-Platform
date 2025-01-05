from datetime import datetime
from RegexGenerator import RegexGenerator
import hashlib
import uuid
from uuid import UUID
from operator import concat
import requests

# https://docs.python.org/3/library/hashlib.html
def generate_token( attrib1: str,attrib2: str,attrib3: str,
                       attrib4: str,attrib5: str,attrib6: str,
                       attrib7: str,attrib8: str,attrib9: str)-> str:
    start_datetime = datetime.now()
    processed_objectname = "generate_token"
    try:
        hash_dataset = ""
        if (attrib1 != None):
            hash_dataset = attrib1
        if (attrib2 != None):
            hash_dataset = concat(hash_dataset,attrib2)
        if (attrib3 != None):
            hash_dataset = concat(hash_dataset,attrib3)
        if (attrib4 != None):
            hash_dataset = concat(hash_dataset,attrib4)
        if (attrib5 != None):
            hash_dataset = concat(hash_dataset,attrib5)
        if (attrib6 != None):
            hash_dataset = concat(hash_dataset, attrib6)
        if (attrib7 != None):
            hash_dataset = concat(hash_dataset, attrib7)
        if (attrib8 != None):
            hash_dataset = concat(hash_dataset, attrib8)
        if (attrib9 != None):
            hash_dataset = concat(hash_dataset, attrib9)
        print(f"Attributes:  {hash_dataset} ")
        hash_value = hashlib.sha512(hash_dataset.encode('utf-8')).hexdigest()
    except (Exception) as error:
        print(f"Error: on {hash_dataset}" + str(error))
    finally:
        return hash_value

def generate_guid(data_attribute: str)-> UUID:
    start_datetime = datetime.now()
    processed_objectname = "generate_token"
    try:
        # Generate a random UUID
        random_uuid = uuid.uuid4()
    except (Exception) as error:
        print(f"Error: on {random_uuid}" + str(error))
    finally:
        # Print the UUID
        return random_uuid

def request_bearer_token(url, user_name, password):
    start_datetime = datetime.now()
    processed_objectname = "request_bearer_token"
    try:
        auth_url = url
        auth_data = {
            'username': user_name,
            'password': password
        }
        response = requests.post(auth_url, data=auth_data)
        token = response.json().get('access_token')
    except (Exception) as error:
        print("Error: on request bearer_token for url: {url}" + str(error))
    finally:
        return token

def request_webbased_data(url):
    start_datetime = datetime.now()
    processed_objectname = "request_webbased_data"
    try:
        web_response_data = requests.post(url)
    except (Exception) as error:
        print("Error: on request of web data for url: {url}" + str(error))
    finally:
        return web_response_data


if __name__ == '__main__':
    # Hashcode Generator Example
    attrib1 = "FirstName"
    attrib2 ="LastName"
    attrib3 ="123303030"
    attrib4 ="6159999999"
    attrib5 ="A12345609LS"
    attrib6 ="37067"
    attrib7 ="asasaaas"
    attrib8 ="aaaa"
    attrib9 ="aaaa"
    returned_data = generate_token(attrib1=attrib1,attrib2=attrib2,attrib3=attrib3,attrib4=attrib4,
                             attrib5=attrib5, attrib6=attrib6,attrib7=attrib7,attrib8=attrib8,attrib9=attrib9)
    print(f"UUID Generation Value(s): attrib1: {attrib1}, attrib2:{attrib2}, attrib3:{attrib3}, attrib4:{attrib4}, "
          f"attrib5:{attrib5}, attrib6:{attrib6}, attrib7:{attrib7}, attrib8:{attrib8},attrib9: {attrib9}")
    print(f"UUID Generation Response: {returned_data}")
    print(f"UUID Generation Response - Count: {len(returned_data)}")

    # UUID Example
    #data_value="ABCD"
    #uid_value:UUID = generate_guid(data_attribute=data_value)
    #print(f"UUID Generation Value: {data_value}")
    #print(f"UUID Generation Response: {uid_value}")