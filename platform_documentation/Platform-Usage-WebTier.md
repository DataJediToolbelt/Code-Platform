<a href="../README.md" target="_blank">Main Page</a>

# Key Technical Capabilities Provided
The following are key technical capabilities the platform provides. The platform
is intended to have two specific application types it supports with its core codebase,
an application (main.py) and web tier for web and apis (app.py).

### Web Tier
1. Platform startup, app.py
2. Settings are loaded.
3. Use the web application and navigate to the appropriate item and follow the prompts
4. Any platform interactions will produce an auditing table entry.


### APIs
1. Platform startup, app.py.
2. Settings are loaded.
3. Access the datatier generation API and using the parameters data will be generated.
4. An auditing transaction will be created for tracking but as of the first release of the APIs 
nothing will be saved.

## Generating Data 
Generating data within the platform is how the platform grows its data. This is known 
as the datatier subsystem of the platform.

## Retrieving Generated Data
Retrieving generated data within the platform is intended to be how the platform
is used by users to get specific generated data they request.

## Anonymyzing Data
This feature is slated to be developed in 11/2024 post all the code being in place
for the platform overall.
