from .config import PATH, PDF_REPORT_JOB_FOLDER
from .security import get_access_token
from .process_job import process_job
from .logging import logger
from croniter import croniter
from datetime import datetime
import json
import shutil


class PDF_report:
    def __init__(self) -> None:
        self.job = None

    def execute(self, job):

        # Copy <your_job>.json         
        if not PDF_REPORT_JOB_FOLDER == None:
            src="{}{}".format(PDF_REPORT_JOB_FOLDER, job)
            des="{}jobs/{}".format(PATH, job)
            shutil.copy(src, des)
        
        # Open the json file
        file = open("{}jobs/{}".format(PATH, job), "r")
        job_detail = json.load(file)
        file.close()

        # Check if selected job is active
        if not job_detail["active"]:
            logger.info("Job {} ist not active".format(job))
            return 0

        # Check selected job timing
        if not croniter.match(job_detail["schedule"], datetime.now()):
            return 0

        #Copy <your_job>.tex
        if not PDF_REPORT_JOB_FOLDER == None:
            src="{}{}".format(PDF_REPORT_JOB_FOLDER, job_detail["filename"])
            des="{}latex/{}".format(PATH, job_detail["filename"])
            shutil.copy(src, des)

        

        # Get access-token via API-Login
        logger.info("Get access token")
        access_token = get_access_token()
        logger.info("Got access token")

        # process the selected job
        logger.info("Proccessing job: {}".format(job))
        process_job(access_token, job_detail)
        logger.info("finished job: {}".format(job))
