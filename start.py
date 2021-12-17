from supersetpdfreport.pdf_report import PDF_report
#from pdf_report.nextcloud import copy_to_cloud

job_name = "example_job.json"

pdf_report_task = PDF_report()
pdf_report_task.execute(job_name)

#copy_to_cloud()