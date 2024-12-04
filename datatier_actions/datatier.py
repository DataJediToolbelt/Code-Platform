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

def query_datatierdata_general(platform_vars, platform_settings, sql_connection, table_name)->list:
    try:
        # Auditing
        start_datetime = datetime.now()
        # Code
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+table_name
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="datatier", operation_name="query_"+table_name,
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
        print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
    finally:
        sql_cursor.close()
        return data_dtls

def query_datatierdata_general_activerecords(platform_vars, platform_settings, sql_connection, table_name)->list:
    try:
        # Auditing
        start_datetime = datetime.now()
        # Code
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+table_name+" where status_id='Active' "
        sql_cursor.execute(sql_query)
        rec_count = sql_cursor.rowcount
        if (rec_count >= 100):
            data_dtls = sql_cursor.fetchmany(100)
        else:
            data_dtls = sql_cursor.fetchall()

        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="datatier", operation_name="query_"+table_name+"_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
        print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
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
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
        #query_refdata_statuses(sql_connection=postgres_sql_connection)
        #create list of all reference tables
        # Omitted - datatier_sdp_dataattributes as it has over 1.58 million recs when loaded
        datatier_tables = ["datatier_crawlers","datatier_sdp_dataattributes",
                           "datatier_sdp_datastructures","datatier_tokens"]
        for table_name in datatier_tables:
            query_datatierdata_general(platform_vars=platform_vars, platform_settings=platform_settings,
                                       sql_connection=postgres_sql_connection, table_name=table_name)
            query_datatierdata_general_activerecords(platform_vars=platform_vars,platform_settings=platform_settings,
                                       sql_connection=postgres_sql_connection, table_name=table_name)
