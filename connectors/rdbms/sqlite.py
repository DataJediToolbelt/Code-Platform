import sqlite3
from datetime import datetime
import os

# https://www.bing.com/search?q=sqlite+in+python&qs=OS&pq=sqllite+in+python&sc=10-17&cvid=0165D0DB98654814A260D50970313E58&FORM=QBRE&sp=1&ghc=1&lq=0
def connect(db_location)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    sql_connection = None
    try:
        #sql_connection = sqlite3.connect(db_location+'datajeditoolbelt.db')
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
        # Create a cursor object using the cursor() method
        #cursor = sql_connection.cursor()
        # Query data
        #cursor.execute("SELECT * FROM datamodel_datatables")
        #rows = cursor.fetchall()
        #for row in rows:
        #    print(row)
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        return sql_connection

if __name__ == "__main__":
    start_time = datetime.now()
    component_name = "platform_processor"
    processing_run_datetime = datetime.now()
    processing_objectname = ""
    operation_name = None
    output_settings = None
    auditing = True
    datatier_technologies = None
    platform_datatier = None
    # Local Variables
    local_path = (os.getcwd())
    local_path = local_path[:-16]
    local_database_path = local_path + os.sep + "platform_data_local" + os.sep
    # Database Connection
    sql_connection = connect(local_database_path)
    print(f"Connection to Local SQLite Ended at {datetime.now()}")