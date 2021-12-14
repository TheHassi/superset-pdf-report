from .nextcloud import transfer_file_to_nextcloud
from .config import PATH
from .chart import get_chart_screenshots
from .send_mail import send_mail
from .logging import logger
import sys
import asyncio
import os
import requests
import subprocess


def process_job(access_token, job_detail):

    # compute, cache, download a chart screenshot with IDs
    logger.info("start to compute, cache, download the charts")
    array_chart_id = job_detail["array_chart_id"]
    asyncio.run(get_chart_screenshots(access_token, job_detail["type"], array_chart_id))
    logger.info("finished compute, cache, download of charts")

    # download images via url
    if job_detail["download_images"]:
        logger.info("start download of images")
        for image in job_detail["download_images_url"]:
            f = open("{}latex/images/{}".format(PATH, image["name"]), "wb")
            response = requests.get(image["url"])
            f.write(response.content)
            f.close()
            logger.debug("downloaded image: {}".format(image["name"]))
        logger.info("finished download of images")

    # Creating the PDF
    if job_detail["generate_pdf"]:
        logger.info("generate PDF")

        sp = subprocess.run(
            "cd {}latex/ && pdflatex -halt-on-error -output-directory pdf/ {} | grep '^!.*' -A200 --color=always".format(
                PATH, job_detail["filename"]
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        if not sp.stderr.decode("utf-8") == "":
            logger.error(sp.stderr.decode("utf-8"))

        if sp.stdout.decode("utf-8") == "":
            sp = subprocess.run(
                "cd {}latex/ && pdflatex -halt-on-error -output-directory pdf/ {} | grep '^!.*' -A200 --color=always".format(
                    PATH, job_detail["filename"]
                ),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                shell=True,
            )

            if sp.stdout.decode("utf-8") == "":
                logger.info("pdf created")
            else:
                logger.error(sp.stdout.decode("utf-8"))
                sys.exit(1)
        else:
            logger.error(sp.stdout.decode("utf-8"))
            sys.exit(1)

        try:
            file_name = job_detail["filename"].replace(".tex", ".aux")
            file_path = "{}latex/pdf/{}".format(PATH, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

            file_name = job_detail["filename"].replace(".tex", ".log")
            file_path = "{}latex/pdf/{}".format(PATH, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

            file_name = job_detail["filename"].replace(".tex", ".toc")
            file_path = "{}latex/pdf/{}".format(PATH, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

            file_name = job_detail["filename"].replace(".tex", ".out")
            file_path = "{}latex/pdf/{}".format(PATH, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        except OSError as e:
            logger.error(e)

    if job_detail["use_nextcloud"]:
        transfer_file_to_nextcloud(job_detail)

    if job_detail["E-Mail"]:
        # Sending E-Mail
        logger.info("start to send E-Mails")
        file_name = job_detail["filename"].replace(".tex", ".pdf")
        send_mail(job_detail, "{}latex/pdf/{}".format(PATH, file_name))
        logger.info("Successfully sent email")
