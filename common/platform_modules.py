import connectors.rdbms.sqlite
import sqlite3
import os
from datetime import datetime
# Platform Specific Imports
#import connectors.rdbms.postgresql
#import connectors.rdbms.sqlserver
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config

# def load_configurations(platform_vars, platform_settings):
#     print("Loading synthetic data generators")
#     try:
#         if(platform_settings.datatier_technologies =="sqlite"):
#             # Create a cursor object using the cursor() method
#             sql_connection = connectors.rdbms.sqlite.connect(platform_vars.local_database_path)
#             cursor = sql_connection.cursor()
#             # Query data
#             cursor.execute("SELECT * FROM platform")
#             rows = cursor.fetchall()
#             for row in rows:
#                 print(row)
#     except Exception as e:
#         print("Error while connecting to database and returning data", e)
#     finally:
#         return rows

def load_platform_capabilities(platform_vars, platform_settings):
    print("Loading Platform Operations")
    try:
            # Create a cursor object using the cursor() method
            sql_connection = sqlite3.connect(platform_vars.local_database_path + "platform.db")
            cursor = sql_connection.cursor()
            # Query data
            cursor.execute("SELECT * FROM platform_operations")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error while connecting to database and returning data", e)
    finally:
        return rows


def create_datatier_config(datatier_technologies, local_database_path=None):
    if datatier_technologies == 'sqlite':
        sql_connection = connectors.rdbms.sqlite.connect_configuration(local_database_path)
    if datatier_technologies == 'sqlserver':
        sql_connection = connectors.rdbms.sqlserver.create_conn()