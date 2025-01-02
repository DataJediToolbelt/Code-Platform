import os
from common.data_generation import generate_regexp_quantity,generate_regexp_quantity_withmetadata, generate_address_us
from datatier_classes.platform import platform_datageneration_dataattributes

def generate_data_automated(platform_datageneration_dataattributes):
    datageneration_desc = None
    definition = None
    dataattribute_id = None
    maintained_date = None
    expiration_date = None
    status_id = None
    created_user = None
    quantity = None
    maxrecords_in_source = None
    registeredapp_guid = None
    organization_guid = None
    for data_row in platform_datageneration_dataattributes:
            #i += 1
        for i, datagen_attribute in enumerate(data_row):
            #print(f"Index {i}: {datagen_attribute}")
            if i == 1:
                datageneration_desc = datagen_attribute
            if i == 2:
                definition = datagen_attribute
            if i == 3:
                dataattribute_id =datagen_attribute
            if i == 4:
                maintained_date = datagen_attribute
            if i == 5:
                expiration_date = datagen_attribute
            if i == 6:
                status_id = datagen_attribute
            if i == 7:
                created_user = datagen_attribute
            if i == 8:
                quantity = datagen_attribute
            if i == 9:
                maxrecords_in_source = datagen_attribute
            if i == 10:
                registeredapp_guid = datagen_attribute
            if i == 11:
                organization_guid = datagen_attribute
                generate_regexp_quantity(random_string=definition,generated_count=quantity)
        print("Generated Data")
