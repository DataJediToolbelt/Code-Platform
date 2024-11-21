# Application and Web Tier Platform
As we discussed on the main platform's repository README.md the main focus of our efforts was on data 
and supporting it with an extensible data tier for a very long time. As we built development assets to showcase 
the tremendous data model extensibilities and capabilities we were always underwhelmed overall. In the end it seems to have a combination
of lack of focus and potentially wrong technology for our overall vision. We are notI slighting any technology as used previously. SpringBoot and Node have a very important 
place in hundreds of widely adopted platforms. While we did some cool things with them 
and we did some cool things with the technologies we felt there could be much more we could do.

So, how and why did we choose Python? While other programming languages that we have used have 
adoption and established communities behind them there was something always nagging us, this is
intended to be a very large data driven platform and are we using the right technologies.
For us, the simple answer was no. What would help us drive better technology from our data driven platform than 
a powerful development technology that is a data enabler. Python was the easy choice with this as our core 
need. Python is the widest adopted development technologists when working with data, hands down. There is 
no other technology in the data engineering space with close to the capabilities it provides. Whether it is AI, or
data focused whether that is EDW (Spark/DataBricks/ Snowflake), RDBMS data usage it is a foundational 
enabler. But well beyond the massive community, supported assets being maintained it also has a vast amount 
of other industry leading capabilities whether it is command line, websites, APIs, or automation Python has a large extensible offering.

## Python Technology
We currently have implemented Python v3.9 through various dot releases in 3.12 successfully on multiple operating systems, 
We have leveraged either the download and installers from python.org or simply installed Anacoda. 

<b>We have experienced issues with several libraries on 3.13 still being an issue as of November 20, 2024.</b>

### Python Virtual Environment
We always recommend following all best practices of technologies, one very nice one in Python is
there usage of virtual environments. While we have the venv directory excluded within the .getignore
you must activate or source it depending upon your OS.

Here is one of the thousands of articles that explains virtual environments in Python.
https://python.land/virtual-environments/virtualenv

We used the simple command (while within the specific project directory): python -m venv venv

#### MacOS and Linux
source ./venv/bin/activate

#### Windows
source .\venv\bin\activate

## Libraries Implemented
This section is intended to show any non-builtin/included Python libraries. These are the core
ones we have added (they have carried along the libraries they leverage as well).

### Installing Packages and PIP
PIP manages Python packages, it also must be updated and maintained. 
From the project directory virtual environment.

`
python -m pip install --upgrade pip
`

We have tried to simplify how you can get the platform running, we have put the
packages into a requirements.txt file. Within the project directory virtual 
environment you can run:

`
pip install -r requirements.txt
`

## Security checks on Modules
Security is very important when using any libraries, Python does have a reputation for having
a large amount of modules that are "unsafe". Here is an article from Red Hat about checking for vulnerabilities.

https://www.redhat.com/sysadmin/find-python-vulnerabilities

In order for us to try and mitigate this risk we plan on following a very common path, using pip-audit.
From the project directory, or within the IDE if you are using one:

`
pip install pip-audit
`

Then, simply run

`
pip-audit
`
# Platform
In order to best explain how the Synthetic Data Platform works we have created content
that explains it. Please start <a href="./Platform-Areas.md" target="_blank">here</a>.

| Area                        | Link                                            |
|-----------------------------|-------------------------------------------------|
| General Basics Details of Platform | [Platform Basics](./Platform-Usage-Basics.md)   |  
| Command Line Platform Usage | [Command Line](./Platform-Usage-CommandLine.md) |
| Web Tier Platform Usage     | [Web Tier](./Platform-Usage-WebTier.md)         |

# Platform - Legacy (Non-Python)
In order to best explain how the Synthetic Data Platform works we have created content
that explains it. Please start <a href="./Platform-Areas.md" target="_blank">here</a>.

## APIs - Legacy (Non-Python)
Specific artifacts related to the platform's provided APIs. It should be noted that most of the APIs need refactoring as the data model
itself was completely refactored to help simplify it and provide greater extensibility for the future.

| Area                 | Repository Location                                                                                            | 
|----------------------|------------------------------------------------------------------------------------------------------------|
| SpringBoot-APIs      |https://github.com/SyntheticDataPlatform/APIs-SpringBoot  |
| Node APIs            |https://github.com/SyntheticDataPlatform/APIs-Node    |
| Quarkus APIs         |https://github.com/SyntheticDataPlatform/APIs-Quarkus |

## User Interfaces - Legacy
While there are projects listed, these are aspirational, as we need to refactor the APIs and reimagine the capabilities we want overall.

| Area                 | Repository Location                                                                                           | 
|----------------------|------------------------------------------------------------------------------------------------------------|
| REACTT UI            | Future - https://github.com/SyntheticDataPlatform/UIs-Web-REACT|
| Vue UI               |https://github.com/SyntheticDataPlatform/UIs-Web-Vue|

