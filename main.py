# Python Imports
from datetime import datetime
import os

# Platform Imports
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.platform_modules
from common.platform_modules import load_syntheticdata_generators

def main():
    # Set Platform Variables
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    # Evaluating Need - Connect to platform datatier
    print("Next Step is modules")
    # Build out component that drives data from datatier based on platform_operation
    # for platform_operation of syntheticdata_generation we need to leverage the platform_datageneration
    # Table for all records with status = 1 (active)
    datarows = load_syntheticdata_generators(platform_vars, platform_settings)
    print("Program Ended")


    

if __name__ == "__main__":
    main()