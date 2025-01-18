<a href="./Data-SyntheticData.md" target="_blank">Synthetic Data Main Page</a></br>
<a href="../README.md" target="_blank">Main Page</a>

# Pre-Requisites
To leverage the platform, you must first setup the [platform](Platform-Prerequisites.md).

# Running the Platform
In order to run the platform please follow these steps.

1. In order to start the platform you must have the pre-requisites setup and resolved and then run main.py. In order to do run the program you can use an IDE
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


### Synthetic Data Generation
The platform will starts up in a consistent way. When the platform starts up and the platform uses the 
platform_operation attribute to load the appropriate configuration and platform capability. The default value is 
syntheticdata_generation. 

The platform maintains all the settings and configuration for anything it can generate in the 
platform_datageneration_dataattributes table. 

| Data Attribute          | Purpose                                                                                   |
|-------------------------|-------------------------------------------------------------------------------------------|
| datagentype_id          | Unique GUID for any data generation action                                                |
| datagentype_description | Description of the data generation id created                                             |
| definition              |                                                                                           |
| definition_metadata     |                                                                                           |
| dataattribute_id        | The specific dataattribute being used. These attributes are in refdata_dataattributes     |
| maintained_date         | The date it was created or modified                                                       |
| expiration_date         | By default it is one year after any record creation or maintained                         |
| status_id               | The status of the current record. The platform will only pull active records              |
| maintained_user         | The default user is 'Platform' for records that were imported                             |
| quantity                | The amount of records for the platform to synthetically generate                          |
| maxrecords_in_source    | The record count that the platform uses to determine if any more data should be generated |
| registeredapp_guid      | The value to use to associate a specific application to the record created                |
| organization_guid       | The value to use to associate a specific organization to the record created               |

