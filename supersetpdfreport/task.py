from superset.extensions import celery_app
from celery.utils.log import get_task_logger
from supersetpdfreport.pdf_report import PDF_report
from typing import Any
import logging
import glob

logger = get_task_logger(__name__)
logger.setLevel(logging.INFO)


@celery_app.task(name="reports-pdf.scheduler")
def pdf_report() -> None:

    logger.info("superset_pdf_report started")
    joblist = glob.glob('*.json')

    for job_name in joblist:
        pdf_report_task = PDF_report()
        pdf_report_task.execute(job_name)
    
    
    logger.info("superset_pdf_report finished")
