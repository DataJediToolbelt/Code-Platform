<a href="https://github.com/DataJediToolbelt/Code-DataJediToolbelt/blob/main/profile/README.md" target="_blank">Main Page</a>

# Setting up The Platform for Usage
As with any technology the setup and configuration is critical with how it functions and performs.

## Step 1: Getting the Code and Data Tier 
The first step for this platform is to ensure you have gotten
the Code and Data repositories downloaded. 

### Code Download Options:
Start by going to the [code repository](https://github.com/DataJediToolbelt/Code-DataJediToolkit)

1. Download the latest main branch of code
2. If there are other branches more current than the main branch you download those
3. Get a current release, currently they are just zips of the code and done monthly

### Data Model Deployment
The platform currently supports Spark (Databricks), SnowFlake, SQL Server, Postgres and SQLite (is starting).
Make sure you can connect to one of these RDBMS, or have access to resources that can setup the 
data platform's DDLs for you. Go to the projects 
[DDL repository](https://github.com/DataJediToolbelt/DataTier-DDLs) and 
download the latest DDL that represents your data tier technology.

Load the DDL into the RDBMS using whatever tooling and capabilities you are comfortable with.

### Data Tier: Seeding the Data Platform
To preseed the datatier with all the potential data we provide initially is a decision we
leave in the hands of the implementer. Go to the projects [Data Loader repository](https://github.com/DataJediToolbelt/DataTier-DataLoaders)
and pull down the project.

#### Loading Order
The following is the intended loading order, we have also prefixed the names of the 
specific loader file with a number to try and ensure clarity.

##### Minimal Data Loading
The following will install the base data needed for the platform.

| File  Name                                                     | 
|----------------------------------------------------------------|
| ./InsertScripts-Base/1-ReferenceData.sql                       | 
| ./InsertScripts-Base/2-DatamodelData.sql                       | 
| ./InsertScripts-Base/3-PlatformData.sql                        |

##### Complete Data Loading
The following will load everything initially into the platform. It will
provide billions of data building possibilities/

| File  Name                                                     | 
|----------------------------------------------------------------|
| ./InsertScripts-Base/1-ReferenceData.sql                       | 
| ./InsertScripts-Base/2-DatamodelData.sql                       | 
| ./InsertScripts-Base/3-PlatformData.sql                        |
| /InsertScripts-Base/4-Datatier-SDP-DataAttributes-{Number}.sql |

# Step 3: Configuring the Platform for Usage
This involves going into the local SQLite database and ensuring that the 
core platform is configured. With the base platform when you download it
all the core platform variables are defined in the database, please 
validate and verify they meet your needs.

# Key Technical Capabilities Provided
The following are key technical capabilities the platform provides. The platform
is intended to have two specific application types it supports with its core codebase,
an application (main.py) and web tier for web and apis (app.py).

# Application
The platform operates on the settings configured. While all the settings are important there
are several that will need to configured for users needs and environments. The following 
settings are critical: datatier, platform_datatier, database_settings, and platform_operations

1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation. This setting
determines the action of the platform. To help everyone with the options we have built a table
there is a table in the SQLLite database named pltaform_operations which explains the command 
line options and what they provide.

## Generating Synthetic Data 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.
