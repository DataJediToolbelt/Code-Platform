# https://pynative.com/python-postgresql-tutorial/#h-verify-psycopg2-installation
from datetime import datetime
import os
import psycopg
from psycopg import Error

def create_connection(connection_string):
    try:
        # Use Configuration Settings from SQLite to drive this
        # Conditional based on data being present in database

        # Connect to an existing database
        #conStr = "postgres://postgres:@localhost:5432/datajeditoolbelt"
        postgres_connection = psycopg.connect(connection_string)
        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
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
        if (postgres_connection):
            cursor.close()
    return postgres_connection

def close_connection(postgres_connection):
    try:
        postgres_connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while closing connection to PostgreSQL", error)
    finally:
        postgres_connection.close()
        
if __name__ == "__main__":
    start_time = datetime.now()
    component_name = "postgresql_connect"
    processing_run_datetime = datetime.now()
    print(f"Connection to Postgres started at {datetime.now()}")
    processing_objectname = ""
    operation_name = None
    output_settings = None
    auditing = True
    datatier_technologies = None
    platform_datatier = None
    # Local Variables
    #local_path = (os.getcwd())
    #local_path = local_path[:-16]
    # ocal_database_path = local_path + os.sep + "platform_data_local" + os.sep
    # Database Connection
    sql_connection =  create_connection()
    print(f"Connection to Postgres at {datetime.now()}")