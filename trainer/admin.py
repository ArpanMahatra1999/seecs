from django.contrib import admin

from .models import Trainer, Qualification, Experience

# Register your models here.
admin.site.register([Trainer, Qualification, Experience])
