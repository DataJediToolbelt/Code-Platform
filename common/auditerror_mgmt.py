import datatier_classes.audting_errorhandling as auditdetails
from datetime import datetime, timedelta
import sqlite3
# Code
from datatier_classes.platform import platform_settings

def cleanup_auditerror_platform(platform_vars, platform_settings):
    try:
        start_datetime = datetime.now()
        # Connect to a defined SQL Server database
        if (platform_settings.auditing == True):
            # SQLite
            if (platform_settings.auditing_datatier == "sqlite"):
                rdbms_connection = sqlite3.connect(platform_vars.local_database_path + "error_auditing.db")
                cur = rdbms_connection.cursor()
                # Build Insert Statement
                # Calculate the date from
                day_count = int(platform_settings.auditing_days_cleanup)
                days_ago = datetime.now() - timedelta(days=day_count)
                days_ago_str = days_ago.strftime('%Y-%m-%d')
                # SQL query to retrieve data 1 day or more old
                recordcount_query = """
                                SELECT * FROM ERROR_AUDITING
                                WHERE AUDIT_DATE <= ?
                                """
                cur.execute(recordcount_query, (days_ago_str,))
                data_dtls = cur.fetchall()
                rec_count = len(data_dtls)
                maintenance_query = """
                DELETE FROM ERROR_AUDITING
                WHERE AUDIT_DATE <= ?
                """
                # Execute the query
                cur.execute(maintenance_query, (days_ago_str,))
                # Commit the changes and close the connection
                rdbms_connection.commit()
                print(f"SQL Auditing Operation - Completed")
    except (Exception) as error:
        print("Error while Inserting Auditing Record", error)
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="errror",
                                   component_name="operations", operation_name="cleanup_auditerror_platform",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="",
                                   error_desc=error, processed_objectname="NA", audit_details="NA")
    finally:
        process_auditerror_details(platform_vars, platform_settings, auditerror_type="audit",
                                   component_name="operations", operation_name="cleanup_auditerror_platform",
                                   start_datetime=start_datetime, end_datetime=datetime.now(),
                                   transaction_count=rec_count, error_id="",
                                   error_desc="NA", processed_objectname="NA", audit_details="NA")
        rdbms_connection.close()

def process_auditerror_details(platform_vars, platform_settings, auditerror_type, component_name,
                               processed_objectname, operation_name, transaction_count,
                               start_datetime,end_datetime,error_id, error_desc,audit_details):

    time_details = datetime.now()
    auditdetails
    auditdetails.event_type = auditerror_type
    auditdetails.event_datetime = datetime.now()
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


