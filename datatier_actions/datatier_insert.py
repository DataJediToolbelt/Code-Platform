from datetime import datetime
import os
# Platform Imports
import connectors.sqlite
from connectors.postgresql import create_connection
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details

def insert_datatier_crawlers()->None:
    print(f"Starting Insert/Upsert Operation")


def insert_datatier_sdp_dataattributes(datatier_sdp_datagenerated, platform_vars, platform_settings, rdbms_connection)->None:
    table_name = "datatier_sdp_dataattributes"
    try:
        # Auditing
        start_datetime = datetime.now()
        # Code To Insert

        # Code to Audit
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
            print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
            process_auditerror_details(platform_vars, platform_settings, auditerror_type="error",
                                       component_name="datatier", operation_name="insert_" + table_name,
                                       start_datetime=start_datetime, end_datetime=datetime.now(),
                                       transaction_count=1, error_id="NA",
                                       error_desc=e, processed_objectname="NA", audit_details="NA")
    finally:
        sql_cursor.close()

def insert_datatier_sdp_datastructure()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_datatier_tokens()->None:
    print(f"Starting Insert/Upsert Operation")

if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.postgresql.create_connection(platform_settings.platform_datatier);
