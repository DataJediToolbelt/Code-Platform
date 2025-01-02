import pymssql
from pymssql import Error
from datetime import time, datetime

# https://learn.microsoft.com/en-us/sql/connect/python/pyodbc/step-3-proof-of-concept-connecting-to-sql-using-pyodbc?view=sql-server-ver16

# SQL Server
# pymssql
# https://learn.microsoft.com/en-us/sql/connect/python/pymssql/python-sql-driver-pymssql?view=sql-server-ver16
# https://pypi.org/project/pymssql/
# # https://learn.microsoft.com/en-us/sql/connect/python/pymssql/step-1-configure-development-environment-for-pymssql-python-development?view=sql-server-ver16
# # https://learn.microsoft.com/en-us/sql/connect/python/pymssql/step-3-proof-of-concept-connecting-to-sql-using-pymssql?view=sql-server-ver16#connect-and-query-data

def pyodbc_msssql_rdbms_connection(connection_string):
    try:

        connString = connection_string.split(':')
        hostname = connString[2].split('@')[1]
        uid = connString[1].replace('/', '')
        pwd = connString[2].split('@')[0]
        dbname = connString[3].split('/')[1]

        connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={hostname};DATABASE={dbname};UID={uid};PWD={pwd}'

        rdbms_connection = pymssql.connect(connectionString)
        print("You are connected to MS SQL Server ")
    except (Exception, Error) as error:
        print("Error while connecting to MS SQL Server", error)
    finally:
        return rdbms_connection


def create_connection(connection_string):
    rdbms_connection = None
    try:
        connString = connection_string.split(':')
        # Connect to a defined SQL Server database
        #rdbms_connection = pymssql.connect({rdbms_host},{rdbms_uid},
        #                                        {rdbms_pwd},{rdbms_database}, as_dict=True}
        hostname = connString[2].split('@')[1]
        uid = connString[1].replace('/', '')
        pwd = connString[2].split('@')[0]
        dbname = connString[3].split('/')[1]

        rdbms_connection = pymssql.connect(server=hostname, user=uid, password=pwd, port=1433, database=dbname, as_dict=True)
        print("You are connected to MS SQL Server ")
    except (Exception, Error) as error:
        print("Error while connecting to MS SQL Server", error)
    finally:
        return rdbms_connection

if __name__ == "__main__":
    connection_string = "mssql://sa:Developer123@192.168.1.224:1433/New_DataJediToolbelt"
    rdbms_connection = create_connection(connection_string)
    print("Connection Test completed ")