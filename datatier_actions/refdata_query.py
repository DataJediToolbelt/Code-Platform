from datetime import datetime
import os
# Platform Imports
from connectors.rdbms_postgresql import create_connection
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details

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

def query_refdata_general(platform_vars, platform_settings, sql_connection, table_name)->list:
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
                                   component_name="refdata", operation_name="query_"+table_name,
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
        print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
    finally:
        sql_cursor.close()
        return data_dtls

def query_refdata_general_activerecords(platform_vars, platform_settings, sql_connection, table_name)->list:
    try:
        # Auditing
        start_datetime = datetime.now()
        # Code
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+table_name+" where status_id='Active' "
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="refdata", operation_name="query_"+table_name+"_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
        print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
    finally:
        sql_cursor.close()
        return data_dtls


if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.postgresql.create_connection(platform_settings.platform_datatier);
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
            query_refdata_general(platform_vars=platform_vars,platform_settings=platform_settings,
                                  sql_connection=postgres_sql_connection, table_name=refdata_table)
            query_refdata_general_activerecords(platform_vars=platform_vars, platform_settings=platform_settings,
                                  sql_connection=postgres_sql_connection, table_name=refdata_table)

