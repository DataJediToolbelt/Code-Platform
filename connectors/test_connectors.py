import os
from datetime import datetime
# Platform Imports
import rdbms_postgresql as connect_postgresql
import rdbms_sqlserver as connect_sqlserver
import protocol_hl7 as hl7_protocol_client
import protocol_http as http_protocol_client
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config

if __name__ == "__main__":
    # Local Variables
    start_time = datetime.now()
    print(f"Connectivity tester started at {datetime.now()}")
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);
    connectors = ['postgresql']
    for connector in connectors:
        if (connector == 'postgresql'):
            # Postgres Database Connection
            rdbms_connection =  connect_postgresql.create_connection(platform_settings.platform_datatier)
            print(f"Connection to Postgres at {datetime.now()}")
        if (connector == 'sqlserver'):
            # SQL Server Database Connection
            rdbms_connection = connect_sqlserver.create_connection(platform_settings.platform_datatier)
            print(f"Connection to SQL Server at {datetime.now()}")
        if (connector == 'http'):
            url =""
            http_protocol_client.connect_to_endpoint(url_value=url)
            print(f"Connection to DTTP site Protocol Client at {datetime.now()}")
        if (connector == 'hl7'):
            #HL7 Client
            hl7_protocol_client.hl7_client()
            print(f"Connection to HL7 Protocol Client at {datetime.now()}")

