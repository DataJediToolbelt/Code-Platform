# Python Imports
from datetime import datetime
import os
# Platform Imports
import connectors.rdbms.sqlite
from connectors.rdbms.sqlite import return_connection
from connectors.rdbms.postgresql import create_connection
from connectors.rdbms.sqlserver import create_connection
import common.platform_modules
from common.platform_modules import load_platform_capabilities
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.error_audit_mgmt
from common.error_audit_mgmt import process_auditerror_details
import platform_data_actions
from platform_data_actions import datatier
from platform_data_actions import platform

def main():
    # Set Platform Variables
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    process_auditerror_details(platform_vars, platform_settings,auditerror_type="audit",
                               component_name="platform_startup",operation_name="load_settings",
                               start_datetime=start_datetime, end_datetime=datetime.now(),
                               transaction_count=0,error_id="NA",
                               error_desc="NA",processed_objectname="NA", audit_details="NA")
    #datarows = load_platform_capabilities(platform_vars, platform_settings)
    # Create a connection to the data tier based on settings
    rdbms_connection = None
    if (platform_settings.datatier_technologies == "postgresql"):
        rdbms_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name=platform_settings.platform_operation_name, operation_name="postgres_dbconnect",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=0, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
        # Do platform_operation activities
        if (platform_settings.platform_operation_name == "data_synthetic_generation"):
            list_generated_dataneeds = platform.query_platformdata_general_activerecords(platform_vars=platform_vars,
                    platform_settings= platform_settings, sql_connection=rdbms_connection, table_name="platform_datageneration_dataattributes")
            print("")
        elif(platform_settings.platform_operation_name == ""):
            print("No Operation Defined")
    if (platform_settings.datatier_technologies == "sqlserver"):
        rdbms_connection = connectors.rdbms.sqlserver.create_connection(platform_settings.platform_datatier);
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name=platform_settings.platform_operation_name, operation_name="sqlserver_dbconnect",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=0, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    print("Program Ended")

def localdb_capabilities():
    # intended ti be for local database
    print("Local Database Capabilities")
    # sql_connection = None
    # sql_connection = connectors.rdbms.sqlite.return_connection(local_database_path)
    # cur = sql_connection.cursor()
    # cur.execute("SELECT * FROM datamodel_tables")
    # result = cur.fetchall()
    # Table for all records with status = 1 (active)
    # Need to ensure we have the correct db setting is define
    # sqlite_sql_connection = return_connection(local_database_path)

if __name__ == "__main__":
    main()

