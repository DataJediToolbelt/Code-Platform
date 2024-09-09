# Python
As we discussed on the main platform README.md the main focus of our efforts was on data 
and supporting it with an extensible data tier for a while. As we 
built development assets to showcase the tremendous data model extensibilities and 
capabilities we were always underwhelmed overall. In the end it seems to have a combination
of lack of focus and potentially wrong technology for our overall vision.

I do not want anyone to get defensive or think I am slighting any technology as 
we are huge fans of SpringBoot and Node, we did some cool things with them 
and man are they fantastic overall, but we felt there could be much more we could do in a 
simpler and more enabling long term manner.

So, how and why did we choose Python? While other programming languages that we have used have 
adoption and established communities behind them there was something always nagging us, this is
intended to be a very large data driven platform and are we using the right technologies.
For us, the simple answer was no. What would help us drive better technology from our data driven platform, a 
powerful technology that is a data enabler. Python was the easy choice with this as our core 
need. Python is the widest adopted development technologists
when working with data, hands down. There is no other technology in the data engineering space with
close to the capabilities it provides. Whether it is AI, or data focused whether that is EDW (Spark/DataBricks/
Snowflake), RDBMS data usage it is a foundational enabler. But well beyond the massive community, supported
assets being maintained it also has a vast amount of other industry leading capabilities whether it is
websites, APIs, or automation Python has a large extensible offering.

## Python 
Details about our python implementation.

### Python Version
We currently have implemented Python v3.1

### Python Virtual Environment
We always recommend following all best practices of technologies, one very nice one in Python is
there usage of virtual environments. While we have the venv directory excluded within the .getignore
you must activate or source it depending upon your OS.

Here is one of the thousands of articles that explains virtual environments in Python.
https://python.land/virtual-environments/virtualenv

#### MacOS
source ./venv/bin/activate

### Libraries Implemented
This section is intended to show any non-builtin/included Python libraries. These are the core
ones we have added (they have carried along the libraries they leverage as well).

| Library    | Purpose                                           | 
|------------|---------------------------------------------------|
| rstr       | Random string generator                           |
| pandas     | Top industry leading data library                 |                                   |
| psycopg2   | RDBMS library for PostgreSQL                      |
| pymssql    | RDBMS library for PostgreSQL                      |
| flask      | Web Framework                                     |
| fastpi     | API Franework  <br/>                              |
| keras      | Deep learning library                             |
| matplotlib | Library for visualizations                        |
| nltk       | Natural Language Toolkit                          |        
| pytorch    | A leading AI library for building and training data |
| requests   | Web Requet framework                              |

# The Synthetic Data Platform - Functionality
In order to best explain how the Synthetic Data Platform works we have created content
that explains it. Please start <a href="https://github.com/SyntheticDataPlatform/Python/blob/main/Platform-Areas.md" target="_blank">here</a>.

# The Synthetic Data Platform Legacy Assets: Repository Layout
The following code is legacy and not being maintained. The goal is that in late 2024 or early 2025 these repositories will
be removed as any functionlaity is ported into Python.

## APIs - Legacy
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

