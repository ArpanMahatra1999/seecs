from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from dss.models import DSS


# Create your models here.
class Document(models.Model):

    DOCUMENT_TYPE = (
        ('Application', 'Application'),
        ('Letter', 'Letter'),
        ('Minute', 'Minute'),
        ('Proposal', 'Proposal'),
        ('Report', 'Report'),
        ('Research Paper', 'Research Paper'),
        ('Resume', 'Resume'),
        ('Thesis', 'Thesis'),
        ('Minute', 'Minute'),
        ('Others', 'Others')
    )
    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True, help_text="Write tags separated with commas like 'tag1, tag2, tag3'")
    document_type = models.CharField(max_length=255, choices=DOCUMENT_TYPE, null=True, blank=True)
    file = models.FileField(null=True, blank=True, upload_to='files/document/')

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_submission_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    created_on_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    last_updated_on_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_submission_AD = models.DateField(null=True, blank=True)
    created_on_AD = models.DateField(null=True, blank=True)
    last_updated_on_AD = models.DateField(null=True, blank=True)

    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
