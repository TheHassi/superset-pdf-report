from superset.extensions import celery_app
from celery.utils.log import get_task_logger
from supersetpdfreport.pdf_report import PDF_report
from supersetpdfreport.config import PDF_REPORT_JOB_FOLDER
from supersetpdfreport.logging import logger
import glob


@celery_app.task(name="reports-pdf-scheduler")
def reports_pdf_scheduler() -> None:

    logger.info("superset_pdf_report started")
    joblist = glob.glob("{}*.json".format(PDF_REPORT_JOB_FOLDER))
    logger.info(joblist)

    for job_name in joblist:
        job = job_name.split("/")[-1]
        logger.info("Check Job: {}".format(job))
        pdf_report_task = PDF_report()
        pdf_report_task.execute(job)

    logger.info("superset_pdf_report finished")
