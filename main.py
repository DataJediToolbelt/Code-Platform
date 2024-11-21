# Python Imports
from datetime import datetime
import os
import connectors.rdbms.sqlite
#import connectors.rdbms.postgresql
#import connectors.rdbms.sqlserver
# Platform Imports
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config

def main():
    # Set Platform Variables
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    # Evaluating Need - Connect to platform datatier
    print("Next Step is modules")
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