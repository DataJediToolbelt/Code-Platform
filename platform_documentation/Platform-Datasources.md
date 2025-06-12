<a href="../README.md" target="_blank">Main Page</a>

# Platform Datasources
The platform leverages datasources to help it achieve a variety of 
technology capabilities that addrss business problems.

# Background
A key aspect of any platform is connecting to a variety of datasources.

## Internal Datasources
These specifically relate ONLY to RBMS configurations for databases except
SQLite, SQLite is connected locally within the platform and the database is
located in a specific location. Now, you could modify the code after you download it to
change this capability.

- You will need to create a file in the connectors sub-directory named .env and populate
it with the same name platform_XXXX=, the connectivity string is a real world local network
functioning example of what the connectivity string looks like.

Postgresql Sample Entry:

`
platform_postgresql="postgres://postgres:@localhost:5432/datajeditoolbelt"
`

SQL Server Sample Entry:

`
platform_SQLServer="mssql://developer:Developer123@192.168.1.224:1433/DataJediToolbelt"
`

## External DataSources
Within the platform any external datasource that the platform will be leveraging is defined within
the table platform_datasources.

### Platform_Datasources Fields


| Field Name      | Purpose | Example| 
|-----------------|--------------|--------|
| Account Numbers | Generated        |Basic Generic Account Number - Built on RegEx|


