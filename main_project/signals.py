from django.db.models import signals
from django.dispatch import receiver
from . import models
from . import tasks


@receiver(signals.post_save, sender = models.Contact)
def post_save_create_contact(sender, instance, created, **kwargs):
    if created:
        tasks.send_email_client.delay(instance.client_name ,instance.client_email)


@receiver(signals.post_save, sender = models.ProjectRequest)
def post_save_create_contact(sender, instance, created, **kwargs):
    if created:
        tasks.project_request.delay(
            instance.project_type,
            instance.message ,
            instance.email,
        )