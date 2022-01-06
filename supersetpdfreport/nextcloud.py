from .config import PATH, NEXTCLOUD_URL, NEXTCLOUD_USER, NEXTCLOUD_PASSWORD
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
    if not client.check(job_detail["nextcloud_folder"]):
        client.mkdir(job_detail["nextcloud_folder"])
        logger.debug(
            "Create Folder {} on nextcloud done".format(job_detail["nextcloud_folder"])
        )

    # Filetransfer
    file_name = job_detail["filename"].replace(".tex", ".pdf")
    file_name_date = job_detail["filename"].replace(
        ".tex", "_{}.pdf".format(datetime.today().strftime("%d_%m_%Y"))
    )
    try:
        client.upload_sync(
            remote_path="{}/{}".format(job_detail["nextcloud_folder"], file_name_date),
            local_path="{}/latex/pdf/{}".format(PATH, file_name),
        )
    except Exception as e:
        logger.error(e)
        sys.exit(1)
