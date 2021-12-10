# superset-pdf-report

superset-pdf-report is a Python tool for downloading charts from the apache-superset-api or URLs, generate a pdf-report via Latex and send it via E-Mail.

There are two possiblilities for using this tool:

- run it by Celery via supersetconfig.py
- run it via Class PDF-report()

## Installation

### PIP Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install superset-pdf-report.

```bash
pip install superset-pdf-report
```
### Configuration of superset-pdf-report

Open config.py in supersetpdfreport and enter the needed information or use the suggested environment variable

### Create your job
Create a <your_job>.json in supersetpdfreport/jobs
 
Use the example_job.json

## Configuration and start via Celery

Insert in superset_config.py

Celeryconfig
```bash
CELERY_IMPORTS = 'supersetpdfreport.task'
```

Add task in CELERYBEAT_SCHEDULE
```bash
'pdf-report':{
    'task':'pdf-report',
    'schedule': crontab(<YOUR TIMING>),
    'kwargs':{
        'job_name': '<your_job>.json'
    },
}
```

You have to restart your apache-superset application for this changes.

## Start via PDF_report()

Create a start.py
```bash
from supersetpdfreport.pdf_report import PDF_report

job_name = "<your job>.json"

pdf_report_task = PDF_report()
pdf_report_task.execute(job_name)
```

Start the Python-Script
```bash
python3 start.py
```

## Usage

1. download the charts you need for the report
2. download the images you need for the report
3. Create your Latex file in /latex and use the images in latex/images
4. activate the "generate_pdf" in job
5. send it via E-Mail
