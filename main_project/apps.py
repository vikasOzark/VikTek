from django.apps import AppConfig
from django.contrib.auth import signals

class MainProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main_project'

    def ready(self):
        import main_project.signals