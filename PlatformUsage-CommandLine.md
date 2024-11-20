<a href="https://github.com/DataJediToolbelt/Code-DataJediToolbelt/blob/main/profile/README.md" target="_blank">Main Page</a>

# Key Technical Capabilities Provided
The following are key technical capabilities the platform provides. The platform
is intended to have two specific application types it supports with its core codebase,
an application (main.py) and web tier for web and apis (app.py).


### Application
1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation as
this determines the action the platform will take. For generating data is data-anon
This will invoke the method(s) that create guids and/or sha-512 hash codes to be used
as key reference for input data so no native values are stored during this process.
3. The keyed data hashes are then reviewed against the platform and either a related 
dataset is retrieved or a dataset linkage in created. This linkage will be permanent. 
4. Upserting (inserting) data into the appropriate table(s) and auditing table.

# Application
1. Platform startup, main.py
2. Settings are loaded and the key setting that is evaluated is platform_operation as
this determines the action the platform will take. For generating data is data-generation.
This will invoke the method(s) that query the relevant platform_ tables.
3. The appropriate data generation methods are invoked 
4. Upserting (inserting) data into the datatier_ table(s) and auditing table.

## Generating Data 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.

## Viewing Platform Data and Managing Platform 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.