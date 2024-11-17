# https://docs.python.org/3/library/sqlite3.html
import sqlite3

def connect_config():
    con = sqlite3.connect("/platform_data_local/configuration.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM configuration_details")
    result= cur.fetchall()
    # loop through the rows
    for row in result:
        print(row)
        print("\n")

if __name__ == "__main__":
    connect_config()