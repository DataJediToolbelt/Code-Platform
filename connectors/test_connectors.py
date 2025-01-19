import os
from datetime import datetime
import sqlite3
from dotenv import load_dotenv, dotenv_values
# Platform Imports
import rdbms_postgresql as connect_postgresql
import rdbms_sqlserver as connect_sqlserver
import protocol_hl7 as hl7_protocol_client
import protocol_http as http_protocol_client
import datatier_actions.platform_query as datatier_actions
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config


def localdb_connectivity(db_location :str)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    sql_connection = None
    try:
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
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
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars);
    # Return table platform_datasources to iterate through active ones
    rdbms_connection = None

    if (platform_settings.datatier_technologies == 'sqlite'):
        rdbms_connection = localdb_connectivity(local_database_path)
    elif (platform_settings.datatier_technologies == 'postgresql'):
        rdbms_connection = connect_postgresql.create_connection()
    elif (platform_settings.datatier_technologies == 'sqlserver'):
        rdbms_connection = connect_postgresql.create_connection()
    platform_datasources = datatier_actions.query_platformdata_general_activerecords(platform_vars = platform_vars, platform_settings =
                                                              platform_settings, sql_connection = rdbms_connection,
                                                              table_name = 'platform_datasources')
    # populate from database entry
    print(f"")
    load_dotenv()
    # Change to be the value in the DATASOURCE_NAME to ensure there is a match
    uid_pwd = os.getenv("SQL_Server")
    connectors = ['postgresql']
    for connector in connectors:
        if (connector == 'postgresql'):
            # Postgres Database Connection
            rdbms_connection =  connect_postgresql.create_connection()
            print(f"Connection to Postgres at {datetime.now()}")
        if (connector == 'sqlserver'):
            # SQL Server Database Connection
            rdbms_connection = connect_sqlserver.create_connection()
            print(f"Connection to SQL Server at {datetime.now()}")
        if (connector == 'http'):
            url =""
            http_protocol_client.connect_to_endpoint(url_value=url)
            print(f"Connection to DTTP site Protocol Client at {datetime.now()}")
        if (connector == 'hl7'):
            #HL7 Client
            hl7_protocol_client.hl7_client()
            print(f"Connection to HL7 Protocol Client at {datetime.now()}")

