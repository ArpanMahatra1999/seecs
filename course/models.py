from ckeditor.fields import RichTextField

from django.db import models


# Create your models here.
class Course(models.Model):
    COURSE = (
        ('Agriculture', 'Agriculture'),
        ('Tourism', 'Tourism'),
        ('Construction', 'Construction')
    )
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, choices=COURSE)
    description = RichTextField(null=True, blank=True)

    def __str__(self):
        return self.title
