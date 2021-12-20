import os
import logging
from pathlib import Path


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
SUPERSET_API_USER = os.environ.get("SUPERSET_API_USER")
SUPERSET_API_PASSWORD = os.environ.get("SUPERSET_API_PASSWORD")

# Configuration for E-Mail Account
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_MAIL_FROM = os.environ.get("SMTP_MAIL_FROM")
SMTP_STARTTLS = False
SMTP_SSL = True

# Configuration for nextcloud webdav
NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL")
NEXTCLOUD_USER = os.environ.get("NEXTCLOUD_USER")
NEXTCLOUD_PASSWORD = os.environ.get("NEXTCLOUD_PASSWORD")
NEXTCLOUD_FOLDER = os.environ.get("NEXTCLOUD_FOLDER")
