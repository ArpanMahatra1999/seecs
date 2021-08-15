from django.db import models
from course_class.models import CourseClass
from datetime import datetime


# Create your models here.
class Notification(models.Model):
    message = models.TextField(null=True, blank=True)
    course_class = models.ForeignKey(CourseClass, null=True, blank=True, on_delete=models.SET_NULL)
    date_and_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.message
