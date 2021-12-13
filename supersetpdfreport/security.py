from .config import SUPERSET_URL, SUPERSET_API_USER, SUPERSET_API_PASSWORD
from .logging import logger
import requests
import json
import sys
import time


# ----------------------------------------------------------
# Get a new access token
# ----------------------------------------------------------
def get_access_token() -> str:
    username=SUPERSET_API_USER
    password=SUPERSET_API_PASSWORD

    retry = 0

    RequestBody = '{"password": "'+password + \
        '","provider": "db", "username": "'+username+'"}'

    while(True):
        try:
            response = requests.post(
                '{}/api/v1/security/login'.format(SUPERSET_URL), json=json.loads(RequestBody))
            if response.status_code == 200 or response.status_code == 202:
                token = response.json()
                access_token = token["access_token"]
            elif response.status_code == 401:
                logger.error("Authentication failed. Exit program")
                sys.exit(2)
            elif response.status_code == 404:
                if retry <10:
                    logger.warning("Host for access token not reached. Retry after 30s")
                    retry=+1
                    time.sleep(30)
                    continue
                else:
                    logger.error("host not reached for authentication")
                    sys.exit(2)
            else:
                logger.error("{}: {}".format(response.status_code, response.text))
            return access_token
        except Exception as e:
            logger.error(e)
            sys.exit(2)