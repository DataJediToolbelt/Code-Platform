from datetime import datetime
import os
# Platform Imports
import connectors.sqlite
from connectors.postgresql import create_connection
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details

def insert_refdata_applications()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_codeset()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_codeset_crossmaps()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_companies()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_devicetypes()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_industries()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_industrystds()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_legalentities()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_operationtype()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_organizations()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_rulesets()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_rulesets_defintions()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_sensitivityflags()->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_statuses(sql_connection)->None:
    print(f"Starting Insert/Upsert Operation")

def insert_refdata_vendors()->None:
    print(f"Starting Insert/Upsert Operation")

if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    if (platform_settings.datatier_technologies == "postgresql"):
        postgres_sql_connection = connectors.postgresql.create_connection(platform_settings.platform_datatier);