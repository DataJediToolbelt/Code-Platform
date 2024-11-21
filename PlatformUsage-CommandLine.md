<a href="https://github.com/DataJediToolbelt/Code-DataJediToolbelt/blob/main/profile/README.md" target="_blank">Main Page</a>

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
