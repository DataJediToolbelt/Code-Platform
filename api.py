import datetime
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import os
# Platform Imports
import connectors.rdbms.sqlite
from connectors.rdbms.sqlite import return_connection
from connectors.rdbms.postgresql import create_connection
import common.platform_modules
from common.platform_modules import load_platform_capabilities
import common.platform_settings
from common.platform_settings import build_platform_variables
from common.platform_settings import build_platform_config
import common.error_audit_mgmt
from common.error_audit_mgmt import process_auditerror_details

# https://www.geeksforgeeks.org/python-build-a-rest-api-using-flask/#
# https://medium.com/@CleytonBonamigo/building-a-flask-api-a-step-by-step-guide-e73345717b52

print(f"API Platform Started at {datetime.datetime.now()}")
local_database_path = os.getcwd() + os.sep + "platform_data_local" + os.sep
platform_vars = build_platform_variables();
# Pull in platform configuration settings from configuration database
platform_settings = build_platform_config(platform_vars.local_database_path);
#process_auditerror_details(platform_vars, platform_settings,"audit")
# API loaders
app = Flask(__name__)
# creating an API object
api = Api(app)

# home route that returns below text
# when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
    # Add Auditing

print("Program Ended")

if __name__ == "__main__":
    app.run(debug=True, port=8000)




