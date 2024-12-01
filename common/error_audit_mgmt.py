import data_classes.audting_errorhandling as auditdetails
import datetime
import sqlite3

def process_auditerror_details(platform_vars, platform_settings, auditerror_type, component_name,
                               processed_objectname, operation_name, processing_object_name, transaction_count,
                               start_datetime,end_datetime,error_id, error_desc,audit_details):
    time_details = datetime.datetime.now()

    auditdetails
    auditdetails.event_type = auditerror_type
    auditdetails.event_datetime = datetime.datetime.now()
    auditdetails.event_date = time_details.date()
    auditdetails.event_time = time_details.time()
    auditdetails.component_name = component_name
    auditdetails.processed_objectname = processed_objectname
    auditdetails.operation_name = operation_name
    auditdetails.transaction_count = transaction_count
    auditdetails.start_datetime = start_datetime
    auditdetails.end_datetime = end_datetime
    auditdetails.error_id = error_id
    auditdetails.error_desc = error_desc
    auditdetails.audit_details = audit_details

    try:
        # Connect to a defined SQL Server database
        #rdbms_connection = pymssql.connect("bluekc-ea.database.windows.net", "eaAdmin", "@Blue!EA9", "indepth",as_dict=True)
        if (platform_settings.auditing == True):
            # SQLite
            if (platform_settings.auditing_datatier == "sqlite"):
                rdbms_connection = sqlite3.connect(platform_vars.local_database_path + "error_auditing.db")
                cur = rdbms_connection.cursor()
                # Build Insert Statement
                sqlQuery = '''insert into error_auditing(audit_type, audit_datetime,audit_date, audit_time,
                audit_component, processed_object,transaction_count,audit_details,error_id,
                error_desc,start_datetime,end_datetime,audit_operation) values (?,?,?,?,?,?,?,?,?,?,?,?,?)'''
                val = (auditdetails.event_type,auditdetails.event_datetime,auditdetails.event_date,
                       str(auditdetails.event_time),auditdetails.component_name,
                       auditdetails.processed_objectname,auditdetails.transaction_count,
                       auditdetails.audit_details,auditdetails.error_id, auditdetails.error_desc,
                       auditdetails.start_datetime, auditdetails.end_datetime,auditdetails.operation_name)
                print(f"SQL String: ", sqlQuery)
                print(f"Values Inserting: ", val)
                cur.execute(sqlQuery, val)
                rdbms_connection.commit()
                print(f"SQL Insert Operation - Completed")
    except (Exception) as error:
        print("Error while Inserting Auditing Record", error)
    finally:
        rdbms_connection.close()


