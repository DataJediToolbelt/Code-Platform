from datetime import datetime
from sys import exception
import connectors.rdbms.sqlite
#import connectors.rdbms.postgresql
#import connectors.rdbms.sqlserver
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config

def load_syntheticdata_generators(platform_vars, platform_settings):
    print("Loading synthetic data generators")
    try:
        if(platform_settings.datatier_technologies =="sqlite"):
            # Create a cursor object using the cursor() method
            sql_connection = connectors.rdbms.sqlite.connect(platform_vars.local_database_path)
            cursor = sql_connection.cursor()
            # Query data
            cursor.execute("SELECT * FROM platform_datageneration")
            rows = cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        print("Error while connecting to database and returning data", e)
    finally:
        return rows

def create_datatier_connectivity(datatier_technologies, local_database_path=None):
    if datatier_technologies == 'sqlite':
        sql_connection = connectors.rdbms.sqlite.connect(local_database_path)
    if datatier_technologies == 'sqlserver':
        sql_connection = connectors.rdbms.sqlserver.create_conn()