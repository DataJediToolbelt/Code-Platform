import random
from datetime import datetime

import rstr
from RegexGenerator import RegexGenerator
import exrex
import sqlite3
# Code
from datatier_classes.datatier import datatier_sdp_datagenerated
from datatier_actions.datatier_insert import insert_datatier_sdp_dataattributes
from datatier_classes.platform import platform_datageneration_dataattributes_ind

def generate_regexp_ind(random_string:str,generated_count:int) ->str:
    pattern = fr'{random_string}'
    #random_string: str = rstr.xeger(pattern)
    random_string: str = exrex.getone(random_string)
    return random_string

def generate_regexp_quantity(random_string:str, generated_count:int) ->list:
    pattern = fr'{random_string}'
    complete_list = []
    random_string: str = rstr.xeger(pattern)
    for i in range(generated_count):
        complete_list.append(exrex.getone(random_string))
    return complete_list

def generate_regexp_quantity_withpersist(platform_datageneration_dataattributes_ind, platform_vars, platform_settings, rdbms_connection):
    pattern = fr'{platform_datageneration_dataattributes_ind.definition}'
    complete_list = []
    random_string: str = rstr.xeger(pattern)
    for i in range(platform_datageneration_dataattributes_ind.quantity):
        complete_list.append(exrex.getone(random_string))

    for detailed_data in complete_list:
        #Loop Through List and Persist - Need to create and add metadata object
        datatier_sdp_datagenerated
        datatier_sdp_datagenerated.dataattribute_id = platform_datageneration_dataattributes_ind.dataattribute_id
        datatier_sdp_datagenerated.datagentype_id = platform_datageneration_dataattributes_ind.datagentype_id
        datatier_sdp_datagenerated.param_value = detailed_data
        datatier_sdp_datagenerated.param_value_dtl=None
        datatier_sdp_datagenerated.maintained_date=datetime.now()
        datatier_sdp_datagenerated.organization_guid = platform_datageneration_dataattributes_ind.organization_guid
        datatier_sdp_datagenerated.registeredapp_guid = platform_datageneration_dataattributes_ind.registeredapp_guid
        datatier_sdp_datagenerated.created_user = platform_datageneration_dataattributes_ind.created_user
        # Insert Record
        insert_datatier_sdp_dataattributes(datatier_sdp_datagenerated=datatier_sdp_datagenerated, platform_vars=platform_vars,
                                           platform_settings=platform_settings, rdbms_connection=rdbms_connection)

def generate_address_us(generate_quantity:int,persist_value:str=None)->str:
    complete_address= []
    for i in range(generate_quantity):
        # Base Address Value
        # Setup usable params
        street_directions = ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]
        street_types = ["Lane", "Way", "Drive", "Avenue"]
        # Replace this with a list of names
        street_names = ["Jones", "Smith", "Scott", "Brown", "Williams"]
        # Randomizers
        random.seed()
        random_number_address_number = random.randint(1, 10000)
        random.seed()
        random_street_name = random.choice(street_names)
        random.seed()
        random_street_direction = random.choice(street_directions)
        random.seed()
        random_street_type = random.choice(street_types)
        random.seed()
        random_address_type = random.randint(0, 1)
        # Build Complete Address
        if random_address_type == 0:
            address_string = f"{random_number_address_number} {random_street_name} {random_street_type} {random_street_direction}"
            complete_address.append(address_string)
        else:
            address_string = f"{random_number_address_number} {random_street_name} {random_street_type}"
            complete_address.append(address_string)
         # Return Value
    return complete_address

def list_deduplicater_count(lst):
    return any(lst.count(item) > 1 for item in lst)

def list_deduplicater_clean(lst)->list:
    # Removing duplicates while preserving order
    unique_list = []
    [unique_list.append(item) for item in lst if item not in unique_list]
    return unique_list

def localdb_connectivity(db_location :str)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    sql_connection = None
    try:
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        return sql_connection


if __name__ == '__main__':
    print("Generating data...")
    # Individual Generated Data
    #random_string ='^4[0-9]{12}(?:[0-9]{3})?$'
    #random_string ='^(?!(000|666|9))\d{3}-(?!00)\d{2}-(?!0000)\d{4}$|^(?!(000|666|9))\d{3}(?!00)/\d{2}(?!0000)\d{4}$'
    # SSN
    #random_string ='^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    # Phone Number
    # random_string='^\\d{3}-\\d{4}$'
    # DOB
    #random_string='^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/((19[2-9][4-9]|200[0-9]|201[0-9]|202[0-5]))$'
    # EIN
    #random_string ='^\\d{2}-\\d{7}$'
    # DLN - CA
    # CA - ^[A-Z]{1}[0-9]{8}$
    # IA - ^[A-Z]{3}[0-9]{2}[A-Z]{4}$
    # NV - ^[0-9]{12}$
    #random_string ='^[0-9]{12}$'
    #returned_data = generate_regexp(random_string)

    # Quantity of Generated Data - Only
    returned_data = []
    generate_quantity = 100
    # Addresses - US
    #returned_data = generate_address_us(generate_quantity=generate_quantity)
    #list_of_values = list_deduplicater_clean(returned_data)
    # Common Generated Types
    # SSN
    #random_string = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    #returned_data = generate_regexp_quantity(random_string=random_string, generated_count=generate_quantity)
    #list_of_values = list_deduplicater_clean(returned_data)

    # Quantity of Generated Data - With persistence
    #returned_data = []
    #generate_quantity = 100
    # Addresses - US
    #returned_data = generate_address_us(generate_quantity=generate_quantity)
    # Common Generated Types
    # SSN
    #random_string = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    #generate_regexp_quantity_withpersist(random_string=random_string, generated_count=generate_quantity)

    #Addresses - US
    #returned_data = generate_address_us(generate_quantity=generate_quantity)

    #print(f"Data Returned: {returned_data}")
    #print("Initial - List of Values Count:" ,(len(returned_data)))
    #print("List of Values From Deduper Count: "(len(list_of_values)))
