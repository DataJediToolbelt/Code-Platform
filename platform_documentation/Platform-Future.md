<a href="https://github.com/DataJediToolbelt/Code-DataJediToolbelt/blob/main/profile/README.md" target="_blank">Main Page</a>


<b>We have experienced issues with several libraries on 3.13 still being an issue as of November 20, 2024.</b>

### Python Virtual Environment
We always recommend following all best practices of technologies, one very nice one in Python is
there usage of virtual environments. While we have the venv directory excluded within the .getignore
you must activate or source it depending upon your OS.

Here is one of the thousands of articles that explains virtual environments in Python.
https://python.land/virtual-environments/virtualenv

We used the simple command (while within the specific project directory): python -m venv venv

#### MacOS and Linux

` 
source ./venv/bin/activate
`

#### Windows

`
source .\venv\bin\activate.bat
`
or
`
source .\venv\bin\activate.ps1
`

### Libraries Implemented
This section is intended to show any non-builtin/included Python libraries. These are the core
ones we have added (they have carried along the libraries they leverage as well).

#### Installing Packages and PIP
PIP manages Python packages, it also must be updated and maintained. 
From the project directory virtual environment.

`
python -m pip install --upgrade pip
`
#### Installing Libraries Into the Virtual Environment
We have tried to simplify how you can get the platform running, we have put the
packages into a requirements.txt file. Within the project directory virtual 
environment you can run:

`
pip install -r requirements.txt
`

#### Security checks on Modules
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
