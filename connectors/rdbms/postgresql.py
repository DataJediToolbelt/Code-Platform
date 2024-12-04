# https://pynative.com/python-postgresql-tutorial/#h-verify-psycopg2-installation
from datetime import datetime
import os
import psycopg
from psycopg import Error
from datetime import datetime
# Platform Imports
import connectors.rdbms.sqlite
from connectors.rdbms.sqlite import return_connection
import common.platform_modules
from common.platform_modules import load_platform_capabilities
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.error_audit_mgmt
from common.error_audit_mgmt import process_auditerror_details

def create_connection(connection_string):
    try:
        # Use Configuration Settings from SQLite to drive this
        # Conditional based on data being present in database

        # Connect to an existing database
        #conStr = "postgres://postgres:@localhost:5432/datajeditoolbelt"
        rdbms_connection = psycopg.connect(connection_string)
        # Create a cursor to perform database operations
        cursor = rdbms_connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        #print(postgres_connection.get_dsn_parameters(), "\n")
        # Executing a SQL query
        cursor.execute("SELECT version();")
        # Fetch result
        record = cursor.fetchone()
        print("You are connected to - ", record, "\n")
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if (rdbms_connection):
            cursor.close()
    return rdbms_connection

def close_connection(rdbms_connection):
    try:
        rdbms_connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while closing connection to PostgreSQL", error)
    finally:
        rdbms_connection.close()
        
if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Connection to Postgres started at {datetime.now()}")
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    # Local Variables
    # Database Connection
    rdbms_connection =  create_connection(platform_settings.platform_datatier)
    print(f"Connection to Postgres at {datetime.now()}")