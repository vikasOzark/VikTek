from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template



def contect_mail(client_name=None, client_mail=None):
    message = get_template(
        "main_project/email_template/client_email_contact.html"
        ).render({'client_name': client_name})

    # html_message=msg_html,
    mail = EmailMessage(
    subject="Order confirmation",
    body=message,
    from_email='vixtec.services@gmail.com',
    to=[client_mail],
    )
    mail.content_subtype = "html"
    return mail.send()
    
def     project_request_mail( project_detail=None, Project_type = None, client_mail=None):
    message = get_template(
        "main_project/email_template/project_final.html"
        ).render({'project_type': Project_type, 'project_detail' : project_detail})
        
    # html_message=msg_html,
    mail = EmailMessage(
    subject=f'Your {Project_type}.',
    body=message,
    from_email='vixtec.services@gmail.com',
    to=[client_mail],
    )
    mail.content_subtype = "html"
    return mail.send()



