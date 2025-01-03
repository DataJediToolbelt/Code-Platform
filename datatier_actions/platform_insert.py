from datetime import datetime
import os
import sqlite3
from dotenv import load_dotenv, dotenv_values
# Platform Imports
#from common.platform_modules import load_platform_capabilities
import connectors.postgresql
import connectors.sqlserver
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details
from datatier_classes.platform import platform_datageneration_dataattributes



def insert_platform_dataattributes()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_platform_datageneration()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_platform_datastructures()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_platform_datastructures_dtl()->None:
    print(f"Starting Insert/Upsert Operation")

if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);