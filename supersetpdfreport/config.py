import os
import logging
from pathlib import Path


#Path of the programm folder
PATH = str(Path(__file__).parent.absolute()) + "/"

#Folder for the log files
LOG_FOLDER="{}/logs/".format(PATH)
LOG_LEVEL = logging.INFO

#Configuration for Superset-API
SUPERSET_URL = "http://localhost:8088/api/v1/"
SUPERSET_API_USER = os.environ.get("SUPERSET_API_USER")
SUPERSET_API_PASSWORD = os.environ.get("SUPERSET_API_PASSWORD")

#Configuration for E-Mail Account
SMTP_HOST = os.environ.get("SMTP_HOST")
SMTP_PORT = os.environ.get("SMTP_PORT")
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASSWORD = os.environ.get("SMTP_PASSWORD")
SMTP_MAIL_FROM = os.environ.get("SMTP_MAIL_FROM")
SMTP_STARTTLS = False
SMTP_SSL = True



