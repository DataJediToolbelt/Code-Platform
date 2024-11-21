# https://docs.python.org/3/library/sqlite3.html
import sqlite3
import data_classes.configurations
import os
from datetime import datetime
# Platform Imports
import data_classes.platform
from data_classes.platform import platform_variables
from data_classes.platform import platform_settings

def build_platform_variables() -> platform_variables:
    # Set Platform Variables
    platform_vars = data_classes.platform.platform_variables(start_time=datetime.now(),
                                                             component_name="platform_processor",
                                                             processing_run_datetime=datetime.now(),
                                                             processing_objectname=None,
                                                             local_path=os.getcwd(),
                                                             local_database_path=os.getcwd() + os.sep + "platform_data_local" + os.sep)
    return platform_vars

def build_platform_config(db_location)->platform_settings:
    #Variables
    output_settings = None
    platform_operation_name = None
    datatier_technologies = None
    platform_datatier = None
    referenceapp_guid = None
    organization_guid = None
    #Code
    con = sqlite3.connect(db_location+"configuration.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM configuration_details")
    result= cur.fetchall()
    # loop through the rows
    for row in result:
        rowDetails = data_classes.configurations.configuration_details(row[0],row[1])

    for list_dtl in result:
        for split_list in list_dtl:
            print(split_list)
            if (split_list == 'output_settings'):
                output_settings = str_to_bool(list_dtl[2])
            if (split_list == 'platform_operation'):
                platform_operation_name = list_dtl[2]
            if (split_list == 'auditing'):
                auditing = str_to_bool(list_dtl[2])
            if (split_list == 'datatier'):
                datatier_technologies = list_dtl[2]
            if (split_list == 'platform_datatier'):
                platform_datatier = list_dtl[2]
            if (split_list == 'referenceapp_guid'):
                referenceapp_guid = list_dtl[2]
            if (split_list == 'organization_guid'):
                organization_guid = list_dtl[2]
    # Populate Dataclass
    platform_settings = data_classes.platform.platform_settings(output_settings=output_settings,
                                                             platform_operation_name=platform_operation_name,
                                                             auditing=auditing,
                                                             datatier_technologies=datatier_technologies,
                                                             platform_datatier=platform_datatier,
                                                             referenceapp_guid=referenceapp_guid,
                                                             organization_guid=organization_guid)
    #return(result)
    return platform_settings

def str_to_bool(s):
    return {"true": True, "false": False,"False":False}.get(s.lower(), False)

if __name__ == "__main__":
    build_platform_config()