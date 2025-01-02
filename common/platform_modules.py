import connectors.sqlite


# Platform Specific Imports
#import connectors.rdbms.postgresql
#import connectors.rdbms.sqlserver

def data_generation_processor(list):
    print("Data Generation Processing")

def create_datatier_config(datatier_technologies, local_database_path=None):
    if datatier_technologies == 'sqlite':
        sql_connection = connectors.sqlite.connect_configuration(local_database_path)
    if datatier_technologies == 'sqlserver':
        sql_connection = connectors.sqlserver.create_conn()