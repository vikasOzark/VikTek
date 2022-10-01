from django.contrib import admin
from . import models 

# Register your models here.
admin.site.register(models.ProjectRequest)
admin.site.register(models.Contact)