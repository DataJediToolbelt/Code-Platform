# Python Imports
from datetime import datetime
import os
# Platform Imports
from common.platform_settings import connect_config

# Local Variables
local_path = os.getcwd()
#audit_details
#msg_details
start_time = datetime.now()
# Auditing Variables
component_name = "platform_processor"
processing_run_datetime = datetime.now()
processing_objectname = ""
operation_name = None

"""
Calculating Tasks
a = datetime.datetime.now()
b = datetime.datetime.now()
c = b - a
# c.days, c.seconds
print(f"{c.seconds}")
print(f"{c.microseconds}")
"""
# Read Configuration and populate key values to process along
# This step also has settings to determine if there is a logging output
# for those running the code
#config = platform_configuration()
#platform_operation = config['General']['platform_operation']

# Create a dictionary of base platform queries to enable us to leverage a parameter
# model for retrieval
my_query_dict = {'refdata_status': 'select * from refdata_statuses',
           'datatier': 'select * from datatier',
           'datatier_structures':'select * from datatier_structures'}
key_to_find = 'refdata_status'

# Main Program
def main():
    print(f"Data Jedi ToolBelt Platform Started at {datetime.now()}")
    #print(f"Platform Operation Type: {platform_operation}")

    # Pull in configuration as step1
    connect_config()

    # Future potential usage
    #if key_to_find in my_query_dict:
    #    print(f"Key '{key_to_find}' found with value: {my_query_dict[key_to_find]}")
    #else:
    #    print(f"Key '{key_to_find}' not found.")

    print("Program Ended")

if __name__ == "__main__":
    main()