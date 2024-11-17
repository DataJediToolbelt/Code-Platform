# https://docs.python.org/3/library/sqlite3.html
import sqlite3
import data_classes.configurations
from dataclasses import dataclass

def connect_config(db_location):
    con = sqlite3.connect(db_location+"configuration.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM configuration_details")
    result= cur.fetchall()
    # loop through the rows
    for row in result:
        # rows = (
        #    data_classes.configurations.configuration_details(row[0], row[1])
        #)
        rowDetails = data_classes.configurations.configuration_details(row[0],row[1])
    return(result)

if __name__ == "__main__":
    connect_config()