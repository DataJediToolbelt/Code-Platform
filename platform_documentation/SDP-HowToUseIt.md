<a href="./Data-SyntheticData.md" target="_blank">Synthetic Data Main Page</a></br>
<a href="../README.md" target="_blank">Main Page</a>

# Pre-Requisites
To leverage the platform, you must first setup the [platform](Platform-Prerequisites.md).

# Running the Platform
In order to run the platform please follow these steps.

1. In order to start the platform you must run main.py. In order to do run the program you can use an IDE
or you can type:

`
python main.py
`

2. The platform loads settings from a SQLite database named platform.db from the table named 
configuration_details. The following are key attributes and what they do.

| Data Attribute | Purpose                                                                                                                                                                                       |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| platform_operation | Is very specific named attribute that is defined that determines the action you want the platform to take.                                                                                    |
| datatier | The RDBMS to be used. If you leverage the defaulot SQLite then you will use the datajeditoolbelt.db in the datatier_local directory. Otherwise, you will need to configure the RDBMS setting. |
| platform_datatier | No longer used                                                                                                                                                                                |
| auditing | If auditing is enabled for the platform. True is the default setting for this. The platform uses the SQLite database error_auditing.db database.                                              |
| referenceapp_guid | This is the default application ID that is used and persisted to various tables when data activities occur.                                                                                   |
| organization_guid | This is the default organizational ID that is used and persisted to various tables when data activities occur.                                                                                |
| auditing_datatier | Feature field for enabling auditing to use additional RDBMS                                                                                                                                   |
| auditing_platform_datatier | Not used                                                                                                                                                                                      |
| auditing_cleanup_days | The Number of days to maintain audit and error details in the ERROR_AUDITING table                                                                                                            |

3. The platform uses the datatier attribute to determine the database to leverage, based on that it
will create the appropriate connection based on the connection type. The platform uses a .env file within the
connectors directory. Here are a few examples how a .env file should look:

SQL_Server="mssql://<username>:<password>@<host>:<port>/<databasename>"
Postgresql="postgresql://<username>:<password>@<host>:<port>/<databasename>"

Some known specific things to watch out for are passwords that start with the @ sign will cause
the database connection to fail. 

4. The platform will use the platform_operation attribute to load the appropriate configuration to run the
platform operation. The default value is syntheticdata_generation. The platform maintains all the settings  
for anything it can generate in the platform_datageneration_dataattributes table.
