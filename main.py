# Python Imports
from datetime import datetime
import os
# Platform Imports
import connectors.sqlite
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details, cleanup_auditerror_platform
#from datatier_actions import platform
from builders.data_generation import generate_data_automated

def main():
    # Set Platform Variables and Platform Settings from configuration database
    start_datetime = datetime.now()
    #local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Platform settings from configuration database and Auditing
    platform_settings = build_platform_config(platform_vars.local_database_path);
    #automated AuditDB cleanup
    cleanup_auditerror_platform(platform_vars, platform_settings)
    process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                               component_name="platform_startup", operation_name="load_settings",
                               start_datetime=start_datetime, end_datetime=datetime.now(),
                               transaction_count=0, error_id="NA",
                               error_desc="NA", processed_objectname="NA", audit_details="NA")

    # Platform Capabilities
    # Synthetic Data Generation By RDBMS
    rdbms_connection = None
    list_data_to_generate = []
    # SQLite
    if (platform_settings.platform_operation_name == "syntheticdata_generation" and platform_settings.datatier_technologies == "sqlite"):
            list_data_to_generate = platform.query_platformdata_general_activerecords(platform_vars=platform_vars,
            platform_settings=platform_settings, sql_connection=rdbms_connection, table_name="platform_datageneration_dataattributes")
            #print(list_data_to_generate)
            # list_data_to_generate = platform.query_platformdata_platformdatagenerationdataattributes_activerecords(platform_vars=platform_vars,
            #                                                                           platform_settings=platform_settings,
            #                                                                           sql_connection=rdbms_connection,
            #                                                                           table_name="platform_datageneration_dataattributes")
            pass
    # Postgres
    if (platform_settings.platform_operation_name == "syntheticdata_generation" and platform_settings.datatier_technologies == "postgresql"):
            list_data_to_generate = platform.query_platformdata_general_activerecords(platform_vars=platform_vars,
                                                                                      platform_settings=platform_settings,
                                                                                      sql_connection=rdbms_connection,
                                                                                      table_name="platform_datageneration_dataattributes")
            pass
    # SQL Server
    if (platform_settings.platform_operation_name == "syntheticdata_generation" and platform_settings.datatier_technologies == "sqlserver"):
            list_data_to_generate = platform.query_platformdata_general_activerecords(platform_vars=platform_vars,
                                                                                      platform_settings=platform_settings,
                                                                                      sql_connection=rdbms_connection,
                                                                                      table_name="platform_datageneration_dataattributes")
            pass
    elif (platform_settings.platform_operation_name == ""):
        print("No Operation Defined")

    #Process with the Data Provided
    generate_data_automated(list_data_to_generate,platform_vars, platform_settings, rdbms_connection)

    print("Program Ended")



if __name__ == "__main__":
    main()
    # process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
    #                            component_name=platform_settings.platform_operation_name,
    #                            operation_name="sqlserver_dbconnect",
    #                            start_datetime=start_datetime, end_datetime=datetime.now(),
    #                            transaction_count=0, error_id="NA",
    #                            error_desc="NA", processed_objectname="NA", audit_details="NA")

