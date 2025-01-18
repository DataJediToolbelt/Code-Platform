from datetime import datetime
import os
import sqlite3
from dotenv import load_dotenv, dotenv_values
# Platform Imports
import connectors.rdbms_postgresql
import connectors.rdbms_sqlserver
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
from common.auditerror_mgmt import process_auditerror_details
from datatier_classes.platform import platform_datageneration_dataattributes

def query_platformdata_general(platform_vars, platform_settings, sql_connection, table_name)->list:
    try:
        # Auditing
        start_datetime = datetime.now()
        # General
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from "+table_name
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = sql_cursor.rowcount
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="platform", operation_name="query_"+table_name,
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
    except Exception as e:
        print("Exception in query: " + table_name + " - " + "Error Details: " + str(e))
    finally:
        sql_cursor.close()
        return data_dtls

def query_platformdata_platformdatagenerationdataattributes_activerecords(platform_vars, platform_settings, sql_connection, table_name)->list:
    start_datetime = datetime.now()
    rec_count = 0
    data_dtls = []
    data_dtls_output = []
    try:
        if platform_settings.datatier_technologies == "sqlite":
            sql_connection = localdb_connectivity(platform_vars.local_database_path)
        elif platform_settings.datatier_technologies == "postgresql":
            load_dotenv()
            connection_string = os.getenv("Postgresql")
            sql_connection = connectors.postgresql.create_connection(connection_string)
        elif platform_settings.datatier_technologies == "sqlserver":
            load_dotenv()
            connection_string = os.getenv("SQL_Server")
            sql_connection = connectors.sqlserver.create_connection(connection_string)
        # Code
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from " + table_name + " where status_id='Active' "
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = len(data_dtls)

        for rows in data_dtls:
            platform_datageneration_dataattributes
            platform_datageneration_dataattributes.dataattribute_id = rows[0]
            platform_datageneration_dataattributes.dataattribute_desc = rows[1]
            platform_datageneration_dataattributes.definition = rows[2]
            platform_datageneration_dataattributes.dataattribute_id = rows[3]
            platform_datageneration_dataattributes.maintained_date = rows[4]
            platform_datageneration_dataattributes.expiration_date = rows[5]
            platform_datageneration_dataattributes.status_id = rows[6]
            platform_datageneration_dataattributes.created_user = rows[7]
            platform_datageneration_dataattributes.quantity = rows[8]
            platform_datageneration_dataattributes.maxrecords_in_source = rows[9]
            platform_datageneration_dataattributes.registeredapp_guid = rows[10]
            platform_datageneration_dataattributes.organization_guid = rows[11]
            data_dtls_output.append(platform_datageneration_dataattributes)


    except Exception as e:
        # Auditing
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="errror",
                                   component_name="platform", operation_name="query_" + table_name + "_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="",
                                   error_desc=e, processed_objectname="NA", audit_details="NA")
    finally:
        # Auditing
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="platform", operation_name="query_" + table_name + "_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
        sql_cursor.close()
        return data_dtls_output


def query_platformdata_general_activerecords(platform_vars, platform_settings, sql_connection, table_name)->list:
    start_datetime = datetime.now()
    rec_count = 0
    try:
        if platform_settings.datatier_technologies == "sqlite":
            sql_connection = localdb_connectivity(platform_vars.local_database_path)
        elif platform_settings.datatier_technologies == "postgresql":
            load_dotenv()
            connection_string = os.getenv("Postgresql")
            sql_connection = connectors.postgresql.create_connection(connection_string)
        elif platform_settings.datatier_technologies == "sqlserver":
            load_dotenv()
            connection_string = os.getenv("SQL_Server")
            sql_connection = connectors.sqlserver.create_connection(connection_string)
        # Code
        sql_cursor = sql_connection.cursor()
        sql_query = "select * from " + table_name + " where status_id='Active' "
        sql_cursor.execute(sql_query)
        data_dtls = sql_cursor.fetchall()
        rec_count = len(data_dtls)
    except Exception as e:
        #print("Exception in query: " + table_name + " - " + "Error Details: " +str(e))
        # Auditing
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="errror",
                                   component_name="platform", operation_name="query_" + table_name + "_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="",
                                   error_desc=e, processed_objectname="NA", audit_details="NA")
    finally:
        # Auditing
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="platform", operation_name="query_" + table_name + "_activerecs",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="NA",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
        sql_cursor.close()
        return data_dtls


def localdb_connectivity(db_location :str)->sqlite3.Connection:
    #print(f"Connection to Local SQLite Started at {datetime.now()}")
    sql_connection = None
    try:
        sql_connection = sqlite3.connect(db_location + 'datajeditoolbelt.db')
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        return sql_connection


if __name__ == "__main__":
    start_datetime = datetime.now()
    local_database_path = os.getcwd() + os.sep + "datatier_local" + os.sep
    platform_vars = build_platform_variables();
    # Pull in platform configuration settings from configuration database
    platform_settings = build_platform_config(platform_vars.local_database_path);


    #
    # if (platform_settings.datatier_technologies == "postgresql"):
    #     postgres_sql_connection = connectors.rdbms.postgresql.create_connection(platform_settings.platform_datatier);
    #     #query_refdata_statuses(sql_connection=postgres_sql_connection)
    #     #create list of all reference tables
    #     platform_tables = ["platform_codesets","platform_codesets_industrystds", "platform_codesets_xmaps",
    #                       "platform_databuilding_dataattributes","platform_databuilding_datastructures",
    #                       "platform_datageneration_dataattributes","platform_datasources",
    #                       "platform_datastructures_dtl","platform_rulesets_definitions",
    #                       "platform_tokens_xmaps"]
    #     for table_name in platform_tables:
    #         query_platformdata_general(platform_vars=platform_vars,platform_settings=platform_settings,
    #                                    sql_connection=postgres_sql_connection, table_name=table_name)
    #         query_platformdata_general_activerecords(platform_vars=platform_vars,platform_settings=platform_settings,
    #         sql_connection=postgres_sql_connection, table_name=table_name)

