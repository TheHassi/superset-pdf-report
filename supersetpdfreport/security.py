from .config import SUPERSET_URL, SUPERSET_API_USER, SUPERSET_API_PASSWORD
from .logging import logger
import requests
import sys
import time


# ----------------------------------------------------------
# Get a new access token
# ----------------------------------------------------------
def get_access_token() -> str:
    retry = 0

    Request_Body = {
        "password": SUPERSET_API_PASSWORD,
        "provider": "db",
        "username": SUPERSET_API_USER,
    }

    while True:
        try:
            login_URL="{}/api/v1/security/login".format(SUPERSET_URL)
            response = requests.post(
                login_URL,
                json=Request_Body,
            )
            if response.status_code == 200 or response.status_code == 202:
                token = response.json()
                access_token = token["access_token"]
            elif response.status_code == 401:
                logger.error("Authentication failed. Exit program")
                sys.exit(1)
            elif response.status_code == 404:
                if retry < 10:
                    logger.warning("Host for access token not reached. Retry after 30s")
                    retry += 1
                    time.sleep(30)
                    continue
                else:
                    logger.error("host not reached for authentication")
                    sys.exit(1)
            else:
                logger.error("{}: {}".format(response.status_code, response.text))
            return access_token
        except Exception as e:
            logger.error(e)
            logger.error(login_URL)
            sys.exit(1)
