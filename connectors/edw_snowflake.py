# https://pypi.org/project/snowflake/
import edw_snowflake.connector
from datetime import time, datetime

# Main Program
def create_connection():
    # Define your connection parameters
    conn_params = {
        'user': 'your_username',
        'password': 'your_password',
        'account': 'your_account_identifier',
        'warehouse': 'your_warehouse',
        'database': 'your_database',
        'schema': 'your_schema'
    }

if __name__ == "__main__":
    start_time = datetime.now()
    print(f"Connection to Snowflake started at {datetime.now()}")
    # Establish the connection
    #conn = snowflake.connector.connect(**conn_params)
    start_datetime = datetime.now()
    # Local Variables
    print(f"Connection to Snowflake at {datetime.now()}")



