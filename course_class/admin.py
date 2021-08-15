from django.contrib import admin

from .models import CourseClass, Test, Employment

# Register your models here.
admin.site.register([CourseClass, Test, Employment])