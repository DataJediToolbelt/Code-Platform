import data_classes.audting_errorhandling as auditdetails
import datetime
import pymssql
import sqlite3

def process_audit_details(event_type, component_name, run_datetime, processing_object_name,
                          operation_name,  data, processing_start_time, processing_end_time,
                          object_elapsed_time_seconds, object_elapsed_time_milliseconds):
    auditdetails
    auditdetails.event_type = event_type
    auditdetails.event_datetime = datetime.datetime.now()
    auditdetails.component_name = component_name
    auditdetails.processing_run_datetime = run_datetime
    auditdetails.processing_objectname = processing_object_name
    auditdetails.operation_name = operation_name
    auditdetails.event_special_comments = data
    auditdetails.processing_start_time = processing_start_time
    auditdetails.processing_end_time = processing_end_time
    auditdetails.processing_duration_time_seconds = object_elapsed_time_seconds
    auditdetails.processing_duration_time_milliseconds = object_elapsed_time_milliseconds

    try:
        # Connect to a defined SQL Server database
        #rdbms_connection = pymssql.connect("bluekc-ea.database.windows.net", "eaAdmin", "@Blue!EA9", "indepth",as_dict=True)
        # SQLite

        #con = sqlite3.connect(local_database_path + "platform.db")
        #cur = con.cursor()
        #cur.execute("SELECT * FROM configuration_details")
        #cursor = rdbms_connection.cursor()
        # Build Insert Statement
        sqlQuery = ("insert into platform_audit (audit_type,  audit_datetime,  audit_component, "
                    "processed_object,  audit_operationname, audit_details,  processing_starttime, "
                    "processing_endtime, processing_duration_seconds, processing_duration_milliseconds)  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        val = (auditdetails.event_type,  auditdetails.event_datetime, auditdetails.component_name,
               auditdetails.processing_objectname, auditdetails.operation_name, auditdetails.event_special_comments,
               auditdetails.processing_start_time, auditdetails.processing_end_time, auditdetails.processing_duration_time_seconds,
               auditdetails.processing_duration_time_milliseconds)
        print(f"SQL String: ", sqlQuery)
        print(f"Values Inserting: ", val)
        cursor.execute(sqlQuery, val)
        rdbms_connection.commit()
        print(f"SQL Insert Operation - Completed")
    except (Exception) as error:
        print("Error while connecting to MS SQL Server", error)
    finally:
        rdbms_connection.close()


