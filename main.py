# Python Imports
from datetime import time, datetime
import os
# Platform Imports
from common.configuration_mgmt import platform_configuration

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
config = platform_configuration()
platform_operation = config['General']['platform_operation']

# Main Program
def main():
    print(f"Synthetic Data Platform Started at {datetime.now()}")
    print(f"Platform Operation Type: {platform_operation}")
    print("Program Ended")

if __name__ == "__main__":
    main()