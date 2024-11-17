# Python Imports
from datetime import datetime
import os
import connectors.rdbms.sqlite
#import connectors.rdbms.postgresql
import connectors.rdbms.sqlserver
# Platform Imports
from common.platform_settings import connect_config

def main():
    # Auditing Variables
    start_time = datetime.now()
    component_name = "platform_processor"
    processing_run_datetime = datetime.now()
    processing_objectname = ""
    operation_name = None
    output_settings = None
    auditing = True
    datatier_technologies = None
    platform_datatier = None
    # Local Variables
    local_path = os.getcwd()
    local_database_path = local_path + os.sep + "platform_data_local" + os.sep
    referenceapp_guid = None
    organization_guid = None
    print(f"Data Jedi ToolBelt Platform Started at {datetime.now()}")
    # Pull in configuration data from configuration database
    configuration_details = connect_config(local_database_path)
    # populate variables to use in platform
    for list_dtl in configuration_details:
        for split_list in list_dtl:
            print(split_list)
            if (split_list == 'output_settings'):
                output_settings = list_dtl[2]
            if (split_list == 'platform_operation'):
                operation_name = list_dtl[2]
            if (split_list == 'auditing'):
                auditing = list_dtl[2]
            if (split_list == 'datatier'):
                datatier_technologies = list_dtl[2]
            if (split_list == 'platform_datatier'):
                platform_datatier = list_dtl[2]
            if (split_list == 'referenceapp_guid'):
                referenceapp_guid = list_dtl[2]
            if (split_list == 'organization_guid'):
                organization_guid = list_dtl[2]
    # Evaluating Need - Connect to platform datatier
    # sql_connection = create_datatier_connectivity(datatier_technologies, local_database_path)
    # Build out component that drives data from datatier based on platform_operation
    # for platform_operation of syntheticdata_generation we need to leverage the platform_datageneration
    # Table for all records with status = 1 (active)
    print("Program Ended")

def create_datatier_connectivity(datatier_technologies, local_database_path=None):
    if datatier_technologies == 'sqlite':
        sql_connection = connectors.rdbms.sqlite.connect(local_database_path)
    if datatier_technologies == 'sqlserver':
        sql_connection = connectors.rdbms.sqlserver.create_conn()
    

if __name__ == "__main__":
    main()