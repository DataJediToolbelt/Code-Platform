import random
import rstr
from RegexGenerator import RegexGenerator
import exrex
import hashlib
import uuid
from uuid import UUID

def generate_hashcode( attrib1: str,attrib2: str,attrib3: str,
                       attrib4: str,attrib5: str,attrib6: str,
                       attrib7: str,attrib8: str,attrib9: str)-> str:
    hash_dataset=""
    hash_value = hashlib.sha512(hash_dataset.encode('utf-8')).hexdigest()
    return hash_value

def generate_guid(data_attribute: str)-> UUID:
    # Generate a random UUID
    random_uuid = uuid.uuid4()

    # Print the UUID
    return random_uuid

def generate_regexp(random_string) ->str:
    pattern = fr'{random_string}'
    #random_string: str = rstr.xeger(pattern)
    random_string: str = exrex.getone(random_string)
    return random_string

if __name__ == '__main__':
    generate_hashcode(attrib1="",attrib2="",attrib3="",attrib4="",attrib5="",
                      attrib6="",attrib7="",attrib8="",attrib9="")
    data_value="ABCD"
    uid_value:UUID = generate_guid(data_attribute=data_value)
    random_string ='^4[0-9]{12}(?:[0-9]{3})?$'
    returned_data = generate_regexp(random_string)

    print(f"Random String: {returned_data}")