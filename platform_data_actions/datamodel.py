from datetime import datetime
import os
# Platform Imports
import connectors.rdbms.sqlite
from connectors.rdbms.postgresql import create_connection
import common.platform_modules
from common.platform_modules import load_platform_capabilities
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.error_audit_mgmt
from common.error_audit_mgmt import process_auditerror_details

def query_datamodeldata_genera(sql_connection, table_name)->list:
    try:
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+table_name
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="refdata", operation_name="query_"+table_name,
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except:
        print("Exception in query: " + table_name)
    finally:
        sql_cursor.close()
        return data_dtls

def insert_datatier()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_datastructure()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_datastructure_dtl()->None:
    print(f"Starting Insert/Upsert Operation")



if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
        #query_refdata_statuses(sql_connection=postgres_sql_connection)
        #create list of all reference tables
        datatier_tables = ["datamodel_apis","datamodel_domains",
                           "datamodel_datatables"]
        for table_name in datatier_tables:
            query_datamodeldata_genera(sql_connection=postgres_sql_connection, table_name=table_name)

#
