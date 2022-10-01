
from celery import shared_task
from django.core import mail

from .email import contect_mail, project_request_mail

@shared_task(name='send_email_client')
def send_email_client(client_name, client_mail):
    contect_mail(client_name, client_mail)
        

@shared_task(name='project_request')
def project_request(project_type,project_detail, client_mail):
    project_request_mail(
        project_type,
        project_detail,
        client_mail
        )
        