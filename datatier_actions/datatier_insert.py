from datetime import datetime
import os
import sqlite3
from sqlite3 import Error
# Platform Imports
import connectors.sqlite
from connectors.postgresql import create_connection
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details

def insert_datatier_crawlers()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_sdp_dataattributes(datatier_sdp_datagenerated, platform_vars, platform_settings, rdbms_connection)->None:
    table_name = "datatier_sdp_dataattributes"
    try:
        rdbms_technology = platform_settings.datatier_technologies
        dir_path = platform_vars.local_database_path
        # Auditing
        start_datetime = datetime.now()
        # Code To Insert
        if rdbms_technology == 'sqlite':
            connection_string = dir_path + "datajeditoolbelt.db"
            rdbms_connection = create_connection(connection_string)
            sql_cursor = rdbms_connection.cursor()
            # Build Insert Statement
            sqlQuery = ''' insert into DATATIER_SDP_DATAATTRIBUTES (DATAATTRIBUTE_ID, DATAGENTYPE_ID, PARAM_VALUE,
                                         PARAM_VALUE_METADATA, REGISTEREDAPP_GUID, ORGANIZATION_GUID)
            values (?,?,?,?,?,?) '''
            val = (datatier_sdp_datagenerated.dataattribute_id, datatier_sdp_datagenerated.datagentype_id,
                   datatier_sdp_datagenerated.param_value,datatier_sdp_datagenerated.param_value_dtl,
                   datatier_sdp_datagenerated.registeredapp_guid,datatier_sdp_datagenerated.organization_guid)
            print(f"SQL String: ", sqlQuery)
            print(f"Values Inserting: ", val)
            sql_cursor.execute(sqlQuery, val)
            rdbms_connection.commit()
            # print(f"SQLite Insert Operation - Completed")
        if rdbms_technology == 'sqlserver' or rdbms_technology == 'postgresql':
           print("")
        # Code to Audit
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc="NA", processed_objectname="insert_datatier_sdp_dataattributes", audit_details="NA")
    except Exception as e:
            print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
            process_auditerror_details(platform_vars, platform_settings, auditerror_type="error",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc=e, processed_objectname="insert_datatier_sdp_dataattributes", audit_details="NA")
    finally:
        sql_cursor.close()

def insert_datatier_sdp_datastructure()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_tokens()->None:
    print(f"Starting Insert/Upsert Operation")

def create_connection(connection_string):
    try:
        rdbms_connection = sqlite3.connect(connection_string)
        # Create a cursor to perform database operations
        cursor = rdbms_connection.cursor()
    except (Exception, Error) as error:
        print("Error while connecting to SQLite", error)
    finally:
        return rdbms_connection

if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.postgresql.create_connection(platform_settings.platform_datatier);
