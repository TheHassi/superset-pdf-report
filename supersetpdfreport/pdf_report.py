from .config import PATH
from .security import get_access_token
from .process_job import process_job
from .logging import logger
import json


class PDF_report:
    def __init__(self) -> None:
        self.job = None

    def execute(self, job):

        # Open the json file
        file = open("{}jobs/{}".format(PATH, job), "r")
        job_detail = json.load(file)
        file.close()

        # Check if selected job is active
        if not job_detail["active"]:
            print("Job {} ist not active".format(job))
            return 0

        # Get access-token via API-Login
        logger.info("Get access token")
        access_token = get_access_token()
        logger.info("Got access token")

        # process the selected job
        logger.info("Proccessing job: {}".format(job))
        process_job(access_token, job_detail)
        logger.info("finished job: {}".format(job))
