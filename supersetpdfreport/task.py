from superset.extensions import celery_app
from celery.utils.log import get_task_logger
from supersetpdfreport.pdf_report import PDF_report
from typing import Any
import logging

logger = get_task_logger(__name__)
logger.setLevel(logging.INFO)


@celery_app.task(name="pdf-report")
def pdf_report(job_name: str, *args: Any, **kwargs: Any) -> None:
    logger.info("superset_pdf_report started")

    pdf_report_task = PDF_report()
    pdf_report_task.execute(job_name)

    logger.info("superset_pdf_report finished")
