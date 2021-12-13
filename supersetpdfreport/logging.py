from .config import LOG_FOLDER, LOG_LEVEL
from datetime import datetime
import logging


# Create a custom logger
logger = logging.getLogger("superset_pdf_report")
logger.setLevel(LOG_LEVEL)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler(
    "{}/superset_pdf_report_{}.log".format(
        LOG_FOLDER, datetime.today().strftime("%d_%m_%Y")
    )
)
c_handler.setLevel(LOG_LEVEL)
f_handler.setLevel(LOG_LEVEL)


# Create formatters and add it to handlers
c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)
