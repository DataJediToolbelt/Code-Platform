import pymssql
from pymssql import Error
from datetime import time, datetime

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