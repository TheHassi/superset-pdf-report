import os
import logging
from pathlib import Path

def read_secret_file(var_name):
    filename = os.getenv(var_name)
    assert filename, f"{var_name} not defined"
    with open(filename) as f:
        return f.read()

# Path of the programm folder
PATH = str(Path(__file__).parent.absolute()) + "/"

# Folder for the log files
LOG_FOLDER = "{}/logs/".format(PATH)
LOG_LEVEL = logging.DEBUG

#Folder for the jobs
PDF_REPORT_JOB_FOLDER = os.environ.get("PDF_REPORT_JOB_FOLDER")

# Configuration for Superset-API
HOST_PROTOCOL = os.environ.get("WEBSERVER_PROTOCOL")
HOST_NAME = os.environ.get("WEBSERVER_ADDRESS")
SUPERSET_PORT = os.environ.get("WEBSERVER_PORT")
SUPERSET_URL = "{}://{}:{}".format(HOST_PROTOCOL, HOST_NAME, SUPERSET_PORT)
SUPERSET_API_USER = os.environ.get("SUPERSET_API_USER", read_secret_file("SUPERSET_API_USER_FILE"))
SUPERSET_API_PASSWORD = os.environ.get("SUPERSET_API_PASSWORD", read_secret_file("SUPERSET_API_PASSWORD_FILE"))

# Configuration for E-Mail Account
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD", read_secret_file("SMTP_PASSWORD_FILE"))
SMTP_MAIL_FROM = os.environ.get("SMTP_MAIL_FROM")
SMTP_STARTTLS = False
SMTP_SSL = True

# Configuration for nextcloud webdav
NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL")
NEXTCLOUD_USER = os.environ.get("NEXTCLOUD_USER", read_secret_file("NEXTCLOUD_USER_FILE"))
NEXTCLOUD_PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD", read_secret_file("NEXTCLOUD_PASSWORD_FILE"))
NEXTCLOUD_FOLDER = os.environ.get("NEXTCLOUD_FOLDER")
