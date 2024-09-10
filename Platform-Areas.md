<a href="https://github.com/SyntheticDataPlatform/Python/blob/main/profile/README.md" target="_blank">Main Page</a>

# SDP - Synthetic Data Platform Capabilities
The following content is intended to explain the core capabilities Python
will help us deliver.

# Key Technical Capabilities Provided
The following are key technical capabilities the platform provides. The platform
is intended to have two specific application types it supports with its core codebase,
an application (main.py) and web tier for web and apis (app.py).

## Viewing Platform Data and Managine Platform 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.

### Web Tier
1. Platform startup, app.py
2. Settings are loaded.
3. Use the web application and navigate to the appropriate item and follow the prompts
4. Any platform interactions will produce an auditing table entry.

## Generating Data 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.

### Application
1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation as
this determines the action the platform will take. For generating data is data-generation.
This will invoke the method(s) that query the relevant platform_ tables.
3. The appropriate data generation methods are invoked 
4. Upserting (inserting) data into the datatier_ table(s) and auditing table.

### APIs
1. Platform startup, app.py.
2. Settings are loaded.
3. Access the datatier generation API and using the parameters data will be generated.
4. An auditing transaction will be created for tracking but as of the first release of the APIs 
nothing will be saved.

## Retrieving Generated Data
Retrieving generated data within the platform is intended to be how the platform
is used by users to get specific generated data they request.

### Application
1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation as
this determines the action the platform will take. For retrieving generating data is data-retrieval.
This will invoke the method(s) that query the relevant datatier values and respond
to user requests.
3. Data will be upserted into the appropriate auditing table.

### APIs
1. Platform is up and running with any specific settings.
2. Platform users will leverage the platform apis

## Anonymyzing Data
This feature is slated to be developed in 11/2024 post all the code being in place
for the platform overall.

This processing of data works on hash keys that are created by data received. 
from sending systems. If the data sent (meaning the field order) is changed in any way
then it will render any key and their subsequent relationships null and void. There will
be NO APIs for this capability.

### Application
1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation as
this determines the action the platform will take. For generating data is data-anon
This will invoke the method(s) that create guids and/or sha-512 hash codes to be used
as key reference for input data so no native values are stored during this process.
3. The keyed data hashes are then reviewed against the platform and either a related 
dataset is retrieved or a dataset linkage in created. This linkage will be permanent. 
4. Upserting (inserting) data into the appropriate table(s) and auditing table.
