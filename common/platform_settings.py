# https://docs.python.org/3/library/sqlite3.html
import sqlite3
import os
from datetime import datetime
# Platform Specific Imports
import datatier_classes.configurations
import datatier_classes.platform
from datatier_classes.platform import platform_variables
from datatier_classes.platform import platform_settings
from common.auditerror_mgmt import process_auditerror_details

def build_platform_variables() -> platform_variables:
    # Set Platform Variables
    platform_vars = datatier_classes.platform.platform_variables(start_time=datetime.now(),
                                                                 component_name="platform_startup",
                                                                 processing_run_datetime=datetime.now(),
                                                                 processing_objectname=None,
                                                                 local_path=os.getcwd(),
                                                                 local_database_path=os.getcwd() + os.sep + "datatier_local" + os.sep)
    return platform_vars

def build_platform_config(platform_vars)->platform_settings:
    start_datetime = datetime.now()
    processed_objectname = "insert_datatier_sdp_dataattributes"
    table_name = "configuration_details"
    #Variables
    output_settings = None
    platform_operation_name = None
    datatier_technologies = None
    platform_datatier = None
    referenceapp_guid = None
    organization_guid = None
    auditing = None
    auditing_datatier = None
    auditing_platform_datatier = None
    auditing_days_cleanup = None
    try:
        #Code
        rdbms_connection = sqlite3.connect(platform_vars.local_database_path+"platform.db")
        cur = rdbms_connection.cursor()
        cur.execute("SELECT * FROM configuration_details")
        result= cur.fetchall()
        # loop through the rows
        #for row in result:
        # Process Results
        for row in result:
            # Set Values
            attrib = row[0]
            attrib_value = row[2]
            #print({row[0]},{row[2]})
            if (attrib == 'output_settings'):
                output_settings = str_to_bool(attrib_value)
            if (attrib == 'platform_operation'):
                platform_operation_name = attrib_value
            if (attrib == 'auditing'):
                auditing = str_to_bool(attrib_value)
            if (attrib == 'datatier'):
                datatier_technologies = attrib_value
            if (attrib == 'platform_datatier'):
                platform_datatier = attrib_value
            if (attrib == 'referenceapp_guid'):
                referenceapp_guid = attrib_value
            if (attrib == 'organization_guid'):
                organization_guid = attrib_value
            if (attrib == 'auditing_datatier'):
                auditing_datatier = attrib_value
            if (attrib == 'auditing_platform_datatier'):
                auditing_platform_datatier = attrib_value
            if (attrib == 'auditing_cleanup_days'):
                auditing_days_cleanup = attrib_value
        # Populate Dataclass
        platform_settings = datatier_classes.platform.platform_settings(output_settings=output_settings,
                                                                        platform_operation_name=platform_operation_name,
                                                                        auditing=auditing,
                                                                        datatier_technologies=datatier_technologies,
                                                                        platform_datatier=platform_datatier,
                                                                        referenceapp_guid=referenceapp_guid,
                                                                        organization_guid=organization_guid,
                                                                        auditing_datatier=auditing_datatier,
                                                                        auditing_platform_datatier=auditing_platform_datatier,
                                                                        auditing_days_cleanup=auditing_days_cleanup)
        #return(result)
    except (Exception) as error:
            #print("Exception in query: " + table_name + " - " + "Error Details: " + str(error))
            process_auditerror_details(platform_vars, platform_settings, auditerror_type="error",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc=error, processed_objectname=processed_objectname+"-"+rdbms_connection, audit_details="NA")
    finally:
        return platform_settings

def str_to_bool(s):
    return {"true": True, "false": False,"False":False,"T":True,"F":False}.get(s.lower(), False)

if __name__ == "__main__":
    build_platform_config()