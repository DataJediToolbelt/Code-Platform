# Python Imports
from datetime import datetime
import os
# Platform Imports
import common.platform_settings
import connectors.rdbms.sqlite
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.platform_modules
from common.platform_modules import load_platform_capabilities
from connectors.rdbms.sqlite import return_connection
from connectors.rdbms.postgresql import create_connection

def main():
    # Set Platform Variables
    local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
    # No DataQuery - Just a method to return values
    #sql_connection = None
    #sql_connection = connectors.rdbms.sqlite.return_connection(local_database_path)
    #cur = sql_connection.cursor()
    #cur.execute("SELECT * FROM datamodel_tables")
    #esult = cur.fetchall()
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    # Evaluating Need - Connect to platform datatier
    print("Next Step is available modules")
    # Build out component that drives data from local data tier
    datarows = load_platform_capabilities(platform_vars, platform_settings)
    # for platform_operation of syntheticdata_generation we need to leverage the platform_datageneration
    # Table for all records with status = 1 (active)
    # Need to ensure we have the correct db setting is define
    #sqlite_sql_connection = return_connection(local_database_path)
    # Connect to DataJediToiolbelt
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
    if (platform_settings.datatier_technologies == "sqlserver"):
        print("SQL Server work TBD")
    print("Program Ended")

if __name__ == "__main__":
    main()