# Python Imports
from datetime import datetime
import os
# Platform Imports

import connectors.rdbms.sqlite
from connectors.rdbms.sqlite import return_connection
from connectors.rdbms.postgresql import create_connection
import common.platform_modules
from common.platform_modules import load_platform_capabilities
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.error_audit_mgmt
from common.error_audit_mgmt import process_auditerror_details

def main():
    # Set Platform Variables
    local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    process_auditerror_details(platform_vars, platform_settings,"audit")
    #datarows = load_platform_capabilities(platform_vars, platform_settings)
    # Create a connection to the data tier based on settings
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
        # for platform_operation of syntheticdata_generation we need to leverage the platform_datageneration
    if (platform_settings.datatier_technologies == "sqlserver"):
        print("SQL Server not yet supported")
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

