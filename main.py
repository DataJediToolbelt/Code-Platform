# Python Imports
from datetime import datetime
import os

# Platform Imports
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.platform_modules
from common.platform_modules import load_platform_capabilities

def main():
    # Set Platform Variables
    local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
    # No DataQuery - Just a method to return values
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    # Evaluating Need - Connect to platform datatier
    print("Next Step is available modules")
    # Build out component that drives data from local data tier
    datarows = load_platform_capabilities(platform_vars, platform_settings)
    print("Next Step is run the action requested")
    # for platform_operation of syntheticdata_generation we need to leverage the platform_datageneration
    # Table for all records with status = 1 (active)
    # Need to ensure we have the correct db setting is definef
    print("Program Ended")


if __name__ == "__main__":
    main()