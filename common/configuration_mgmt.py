import configparser
import datetime
import os

def platform_configuration()->configparser:
    base_dir = os.getcwd()
    now = datetime.datetime.now()
    config = configparser.ConfigParser()
    config.read('./settings/settings.ini')
    # Params
    output_settings = config['General']['output_settings']
    platform_op = config['General']['platform_operation']

    # Output
    if output_settings == "True":
        print(f"Program Startup")
        print(f"-------------------")
        print(f"Running Directory: {base_dir}")
        print(f"Date: {now.date()}")
        print(f"Time: {now.time()}")
        print(f"")
        print(f"Configured Settings")
        print(f"-------------------")
        print(f"Parsing Type: {platform_op}")  # -> "/path/name/"
        #print(f"Inbound Connector Type: {inbd_connector_type}")
        #print(f"Outbound Connector Type: {outbd_connector_type}")  # -> "/path/name/"
        #print(f"Industry Std: {industry_std}")  # -> "/path/name/"
        print(f"-------------------")
    # return the config object to calling program
    return config

if __name__ == "__main__":
    platform_configuration()