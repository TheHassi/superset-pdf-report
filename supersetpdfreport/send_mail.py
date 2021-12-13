from .config import (
    SMTP_HOST,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
    SMTP_MAIL_FROM,
    SMTP_STARTTLS,
    SMTP_SSL,
)
from .logging import logger
from pathlib import Path
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import ssl
import smtplib
import sys


def send_mail(job_detail, file_path):

    try:
        if SMTP_SSL:
            ssl_context = ssl.create_default_context()
            smtp = smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=ssl_context)
        elif SMTP_STARTTLS:
            # TODO Test with STARTTLS
            logger.debug("has not been tested")
            smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
            smtp.starttls()

        smtp.connect(SMTP_HOST, SMTP_PORT)
        smtp.set_debuglevel(0)
        smtp.login(SMTP_USER, SMTP_PASSWORD)

        for email in job_detail["mail_recipient"]:
            mail = MIMEMultipart("alternative")
            mail["Subject"] = job_detail["mail_subject"]
            mail["From"] = SMTP_MAIL_FROM
            mail["To"] = email

            text_content = MIMEText(job_detail["mail_text"], "plain")

            mail.attach(text_content)

            # attaching an attachment
            mimeBase = MIMEBase("application", "octet-stream")
            with open(file_path, "rb") as file:
                mimeBase.set_payload(file.read())
                encoders.encode_base64(mimeBase)
                mimeBase.add_header(
                    "Content-Disposition",
                    f"attachment; filename={Path(file_path).name}",
                )
                mail.attach(mimeBase)

            smtp.sendmail(SMTP_MAIL_FROM, str(email), mail.as_string())

        smtp.quit()

    except Exception as e:
        smtp.quit
        logger.error(e)
        sys.exit(1)
