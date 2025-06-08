import os
from datetime import datetime
import sqlite3
from dotenv import load_dotenv, dotenv_values
# Platform Imports
import rdbms_postgresql as connect_postgresql
import rdbms_sqlserver as connect_sqlserver
#import protocol_hl7 as hl7_protocol_client
import protocol_http as http_protocol_client
import datatier_actions.platform_query as datatier_actions
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details
import common.formatters as formatters

def localdb_connectivity(db_location :str)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    platform_vars = build_platform_variables();
    local_database_path = os.path.dirname(os.getcwd()) + os.sep + "datatier_local" + os.sep
    platform_vars.local_database_path = local_database_path
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars);
    sql_connection = None
    try:
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
        component_name="db_connect", operation_name="connect_sqlite", start_datetime=start_datetime,
        end_datetime=datetime.now(), transaction_count=0, error_id="NA", error_desc="NA", processed_objectname="NA",
        audit_details="Connected to SQLite DB")
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit", component_name="db_connect", operation_name="connect_sqlite",
        start_datetime=start_datetime, end_datetime=datetime.now(), transaction_count=0, error_id=error.sqlite_errorcode, error_desc=error, processed_objectname="NA",
        audit_details="Connected to SQLite DB")
    finally:
        return sql_connection

if __name__ == "__main__":
    # Local Variables
    start_time = datetime.now()
    print(f"Connectivity tester started at {datetime.now()}")
    start_datetime = datetime.now()
    platform_vars = build_platform_variables();
    local_database_path = os.path.dirname(os.getcwd()) + os.sep + "datatier_local" + os.sep
    platform_vars.local_database_path = local_database_path
    # Loads hidden .env file for usage
    load_dotenv()
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars);
    # Return table platform_datasources to iterate through active ones

    if (platform_settings.datatier_technologies == 'sqlite'):
        rdbms_connection = localdb_connectivity(local_database_path)
    elif (platform_settings.datatier_technologies == 'postgresql'):
        platform_db = os.getenv("platform_postgresql")
        rdbms_connection = connect_postgresql.create_connection(platform_db)
    elif (platform_settings.datatier_technologies == 'sqlserver'):
        rdbms_connection = connect_postgresql.create_connection()

    if rdbms_connection != None:
        platform_datasources = datatier_actions.query_platformdata_general_activerecords(platform_vars = platform_vars, platform_settings =
                                                              platform_settings, sql_connection = rdbms_connection,
                                                              table_name = 'platform_datasources')
        # loop through returned records and connect to them
        for platform_datasource in platform_datasources:
            print(f"Data source name {platform_datasource}")
            # Loads hidden .env file for usage
            #load_dotenv()
            # Change to be the value in the DATASOURCE_NAME to ensure there is a match
            #uid_pwd = os.getenv("SQL_Server")
            # Build Connection String
            #connection_string = formatters.build_rdbms_connection_string()
            #connectors = ['postgresql']
            #for connector in platform_datasources:
            #if (connector == 'postgresql'):
            if (platform_datasource == 'postgresql'):
                # Postgres Database Connection
                rdbms_connection =  connect_postgresql.create_connection()
                print(f"Connection to Postgres at {datetime.now()}")
            if (platform_datasource == 'sqlserver'):
                # SQL Server Database Connection
                #rdbms_connection = connect_sqlserver.create_connection()
                print(f"Connection to SQL Server at {datetime.now()}")
            if (platform_datasource == 'http'):
                url =""
                http_protocol_client.connect_to_endpoint(url_value=url)
                print(f"Connection to DTTP site Protocol Client at {datetime.now()}")
            if (platform_datasource == 'hl7'):
                #HL7 Client
                #hl7_protocol_client.hl7_client()
                print(f"Connection to HL7 Protocol Client at {datetime.now()}")

