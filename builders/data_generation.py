import os
import sqlite3
from common.data_generation import generate_regexp_quantity,generate_regexp_quantity_withpersist, generate_address_us
from datatier_classes.platform import platform_datageneration_dataattributes_ind

def generate_data_automated(platform_datageneration_dataattributes, platform_vars, platform_settings, rdbms_connection):
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
            if i == 0:
                datagentype_id = datagen_attribute
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
                # build dataclass to pass into method
                platform_datageneration_dataattributes_ind
                platform_datageneration_dataattributes_ind.datagentype_id = datagentype_id
                platform_datageneration_dataattributes_ind.dataattribute_id = dataattribute_id
                platform_datageneration_dataattributes_ind.dataattribute_desc = datageneration_desc
                platform_datageneration_dataattributes_ind.definition = definition
                platform_datageneration_dataattributes_ind.status_id = status_id
                platform_datageneration_dataattributes_ind.quantity = quantity
                platform_datageneration_dataattributes_ind.maxrecords_in_source = maxrecords_in_source
                platform_datageneration_dataattributes_ind.created_user = created_user
                platform_datageneration_dataattributes_ind.maintained_date = maintained_date
                platform_datageneration_dataattributes_ind.expiration_date = expiration_date
                platform_datageneration_dataattributes_ind.registeredapp_guid = registeredapp_guid
                platform_datageneration_dataattributes_ind.organization_guid = organization_guid
                if definition != "generate_address_us":
                    generate_regexp_quantity_withpersist(platform_datageneration_dataattributes_ind=platform_datageneration_dataattributes_ind,platform_vars=platform_vars,
                  platform_settings=platform_settings, rdbms_connection=rdbms_connection)
                else:
                    generate_regexp_quantity_withpersist(platform_datageneration_dataattributes_ind=platform_datageneration_dataattributes_ind,platform_vars=platform_vars,
                  platform_settings=platform_settings, rdbms_connection=rdbms_connection)
        print("Generated Data")

def localdb_connectivity(db_location :str)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    sql_connection = None
    try:
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        return sql_connection