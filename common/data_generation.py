import random
from sqlite3 import complete_statement

import rstr
from RegexGenerator import RegexGenerator
import exrex

def generate_regexp_ind(random_string:str,generated_count:int) ->str:
    pattern = fr'{random_string}'
    #random_string: str = rstr.xeger(pattern)
    random_string: str = exrex.getone(random_string)
    return random_string

def generate_regexp_quantity(random_string:str, generated_count:int) ->str:
    pattern = fr'{random_string}'
    complete_list = []
    #random_string: str = rstr.xeger(pattern)
    for i in range(generated_count):
        complete_list.append(exrex.getone(random_string))
    return complete_list

def generate_address_us(generate_quantity:int)->str:
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


if __name__ == '__main__':
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

    # Quantity of Generated Data
    returned_data = []
    generate_quantity = 100
    # Addresses - US
    #returned_data = generate_address_us(generate_quantity=generate_quantity)
    #list_of_values = list_deduplicater_clean(returned_data)
    # Common Generated Types
    # SSN
    random_string = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    returned_data = generate_regexp_quantity(random_string=random_string, generated_count=generate_quantity)
    list_of_values = list_deduplicater_clean(returned_data)
    #print(f"Data Returned: {returned_data}")
    #print("Initial - List of Values Count:" ,(len(returned_data)))
    #print("List of Values From Deduper Count: "(len(list_of_values)))
    print((""))