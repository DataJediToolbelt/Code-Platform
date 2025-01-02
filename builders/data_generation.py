import os
from common.data_generation import generate_regexp_quantity, generate_address_us

def generate_data_automated(list_data_to_generate):
    for data_row in list_data_to_generate:
        print(data_row)
        generate_regexp_quantity(data_row[1])