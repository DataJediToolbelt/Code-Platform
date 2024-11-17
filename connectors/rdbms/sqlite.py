import sqlite3
from datetime import datetime

# https://www.bing.com/search?q=sqlite+in+python&qs=OS&pq=sqllite+in+python&sc=10-17&cvid=0165D0DB98654814A260D50970313E58&FORM=QBRE&sp=1&ghc=1&lq=0
def connect():

    print(f"Connection to Local SQLite Started at {datetime.now()}")
    # Connect to an SQLite database (or create it if it doesn't exist)
    try:
        conn = sqlite3.connect('../../platform_data_local/datajeditoolbelt.db')
        # Create a cursor object using the cursor() method
        cursor = conn.cursor()

        # Query data
        cursor.execute("SELECT * FROM datamodel_datatables")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)

if __name__ == "__main__":
    connect()