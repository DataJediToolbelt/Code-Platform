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

def query_refdata_vendors(sql_connection)->list:
    core_component = "refdata_vendors"
    try:
        sql_cursor = sql_connection.cursor()
        sql_cursor.execute("SELECT * FROM refdata_vendors")
        vendor_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="refdata", operation_name="query_vendors",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except:
        print("Exception in query: " + {core_component})
    finally:
        sql_cursor.close()
        return vendor_dtls

def query_refdata_genera(sql_connection, refdata_tablename)->list:
    try:
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+refdata_tablename
        sql_cursor.execute(sql_query)
        refdata_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="refdata", operation_name="query_"+refdata_tablename,
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except:
        print("Exception in query: " + refdata_tablename)
    finally:
        sql_cursor.close()
        return refdata_dtls

def insert_refdata_applications()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_codeset()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_codeset_crossmaps()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_companies()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_devicetypes()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_industries()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_industrystds()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_legalentities()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_operationtype()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_organizations()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_rulesets()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_rulesets_defintions()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_sensitivityflags()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_statuses(sql_connection)->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_vendors()->None:
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
        refdata_tables = ["refdata_applications", "refdata_codesets", "refdata_dataattributes",
                          "refdata_datastructures", "refdata_devicetypes", "refdata_industries",
                          "refdata_industries_business","refdata_industrystds",
                          "refdata_industrystds_eventtypes", "refdata_legalentities",
                          "refdata_operationtypes", "refdata_organizations", "refdata_professiontypes",
                          "refdata_rulesets", "refdata_sensitivityflags", "refdata_status",
                          "refdata_terminologystds","refdata_timezones","refdata_usstates","refdata_vendors"]
        for refdata_table in refdata_tables:
            query_refdata_genera(sql_connection=postgres_sql_connection, refdata_tablename=refdata_table)

