from datetime import datetime
import os
import sqlite3
from sqlite3 import Error
from dotenv import load_dotenv, dotenv_values
# Platform Imports
from connectors.rdbms_postgresql import create_connection as postgresql_connector
from connectors.rdbms_sqlserver import create_connection as sqlserver_connector
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details

def insert_datatier_crawlers()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_sdp_dataattributes(datatier_sdp_datagenerated, platform_vars, platform_settings, rdbms_connection)->None:
    table_name = "datatier_sdp_dataattributes"
    start_datetime = datetime.now()
    processed_objectname = "insert_datatier_sdp_dataattributes"
    try:
        rdbms_technology = platform_settings.datatier_technologies
        dir_path = platform_vars.local_database_path
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
            #print(f"SQL String: ", sqlQuery)
            #print(f"Values Inserting: ", val)
            sql_cursor.execute(sqlQuery, val)
            rdbms_connection.commit()
            # print(f"SQLite Insert Operation - Completed")
        if rdbms_technology == 'sqlserver' or rdbms_technology == 'postgresql':
            load_dotenv()
            if rdbms_technology == 'sqlserver':
                connection_string = os.getenv("SQL_Server")
                rdbms_connection = sqlserver_connector.create_connection(connection_string)
                sql_cursor = rdbms_connection.cursor()
                # Build Insert Statement
                sqlQuery = ''' insert into DATATIER_SDP_DATAATTRIBUTES (DATAATTRIBUTE_ID, DATAGENTYPE_ID, PARAM_VALUE,
                                                        PARAM_VALUE_METADATA, REGISTEREDAPP_GUID, ORGANIZATION_GUID)
                           values (%s,%s,%s,%s,%s,%s) '''
                val = (datatier_sdp_datagenerated.dataattribute_id, datatier_sdp_datagenerated.datagentype_id,
                       datatier_sdp_datagenerated.param_value, datatier_sdp_datagenerated.param_value_dtl,
                       datatier_sdp_datagenerated.registeredapp_guid, datatier_sdp_datagenerated.organization_guid)
                #print(f"SQL String: ", sqlQuery)
                #print(f"Values Inserting: ", val)
                sql_cursor.execute(sqlQuery, val)
                rdbms_connection.commit()
            elif rdbms_technology == 'postgresql':
                connection_string = os.getenv("Postgresql")
                rdbms_connection = postgresql_connector.create_connection(connection_string)
                cur = rdbms_connection.cursor()
                # Build Insert Statement
                sqlQuery = ''' insert into DATATIER_SDP_DATAATTRIBUTES (DATAATTRIBUTE_ID, DATAGENTYPE_ID, PARAM_VALUE,
                                                                        PARAM_VALUE_METADATA, REGISTEREDAPP_GUID, ORGANIZATION_GUID)
                                           values (%s,%s,%s,%s,%s,%s) '''
                val = (datatier_sdp_datagenerated.dataattribute_id, datatier_sdp_datagenerated.datagentype_id,
                       datatier_sdp_datagenerated.param_value, datatier_sdp_datagenerated.param_value_dtl,
                       datatier_sdp_datagenerated.registeredapp_guid, datatier_sdp_datagenerated.organization_guid)
                #print(f"SQL String: ", sqlQuery)
                #print(f"Values Inserting: ", val)
                cur.execute(sqlQuery, val)
                rdbms_connection.commit()
                #print(f"SQL Insert Operation - Completed")
        # Code to Audit
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc="NA", processed_objectname="insert_datatier_sdp_dataattributes"+"-"+rdbms_connection, audit_details="NA")
    except (Exception) as error:
            #print("Exception in query: " + table_name + " - " + "Error Details: " + str(error))
            process_auditerror_details(platform_vars, platform_settings, auditerror_type="error",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc=error, processed_objectname=processed_objectname+"-"+rdbms_connection, audit_details="NA")
    finally:
        sql_cursor.close()

def insert_datatier_sdp_datastructure()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_tokens()->None:
    print(f"Starting Insert/Upsert Operation")

def create_connection(connection_string):
    processed_objectname = "create_connection"
    try:
        rdbms_connection = sqlite3.connect(connection_string)
        # Create a cursor to perform database operations
        cursor = rdbms_connection.cursor()
    except (Exception, Error) as error:
        #print("Error while connecting to SQLite", error)
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="error",
                                   component_name=processed_objectname, operation_name="RDBMS Connection",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=1, error_id="NA",
                                   error_desc=error, processed_objectname=processed_objectname+"-"+rdbms_connection, audit_details="NA")
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
