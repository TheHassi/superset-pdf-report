from .config import (
    PATH,
    NEXTCLOUD_URL,
    NEXTCLOUD_USER,
    NEXTCLOUD_PASSWORD,
    NEXTCLOUD_FOLDER,
)
from .logging import logger
from webdav3.client import Client
from datetime import datetime
import sys


def transfer_file_to_nextcloud(job_detail):
    options = {
        "webdav_hostname": NEXTCLOUD_URL,
        "webdav_login": NEXTCLOUD_USER,
        "webdav_password": NEXTCLOUD_PASSWORD,
    }
    client = Client(options)

    # check the nextcloud connection
    logger.debug("Start connection to nextcloud")
    try:
        client.list()
    except Exception as e:
        logger.error(e)
        sys.exit(1)

    # Check for folder on nextcloud
    if not client.check(NEXTCLOUD_FOLDER):
        client.mkdir(NEXTCLOUD_FOLDER)
        logger.debug("Create Folder {} on nextcloud done".format(NEXTCLOUD_FOLDER))

    # Filetransfer
    file_name = job_detail["filename"].replace(".tex", ".pdf")
    file_name_date = job_detail["filename"].replace(
        ".tex", "_{}.pdf".format(datetime.today().strftime("%d_%m_%Y"))
    )
    try:
        client.upload_sync(
            remote_path="{}/{}".format(NEXTCLOUD_FOLDER, file_name_date),
            local_path="{}/latex/pdf/{}".format(PATH, file_name),
        )
    except Exception as e:
        logger.error(e)
        sys.exit(1)
