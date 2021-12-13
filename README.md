# superset-pdf-report

superset-pdf-report is a Python tool for downloading charts from the Apache Superset API or URLs to generate a PDF report via LaTeX and send it via e-mail.

There are two possiblilities for using this tool:

- run it by Celery via supersetconfig.py
- run it via class PDF_report

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install superset-pdf-report.

```bash
pip install superset-pdf-report
```

### Configuration of superset-pdf-report

Open config.py in supersetpdfreport and enter the needed information or use the suggested environment variables.

### Create your job

Create a `<your_job>.json` in supersetpdfreport/jobs
 
Please refer to the example_job.json

## Configuration and start via Celery

Insert in superset_config.py

Celery config:

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

You have to restart your Apache Superset application for this changes.

## Start via PDF_report()

Create a start.py

```bash
from supersetpdfreport.pdf_report import PDF_report

job_name = "<your job>.json"

pdf_report_task = PDF_report()
pdf_report_task.execute(job_name)
```

Start the Python script

```bash
python3 start.py
```

## Usage

1. Download the charts you need for the report
2. Download the images you need for the report
3. Create your LaTeX file in /latex and use the images in latex/images
4. Activate the "generate_pdf" in job
5. Send it via e-mail or send to nextcloud
