# https://pynative.com/python-postgresql-tutorial/#h-verify-psycopg2-installation
import psycopg
from psycopg import Error

def create_conn():
    try:
        # Connect to an existing database
        postgres_connection = psycopg.connect(user="developer",
                                      password="Developer123",
                                      host="Svr2022-DB",
                                      port="5432",
                                      database="DataSynthesis")

        # Create a cursor to perform database operations
        cursor = postgres_connection.cursor()
        # Print PostgreSQL details
        print("PostgreSQL server information")
        print(postgres_connection.get_dsn_parameters(), "\n")
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

def close_conn(postgres_connection):
    try:
        postgres_connection.close()
        print("PostgreSQL connection is closed")
    except (Exception, Error) as error:
        print("Error while closing connection to PostgreSQL", error)
    finally:
        postgres_connection.close()
