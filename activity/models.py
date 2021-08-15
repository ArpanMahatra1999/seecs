from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from nepali_datetime_field.models import NepaliDateField


from dss.models import DSS


# Create your models here.
class Activity(models.Model):

    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    FISCAL_YEARS = (
        ('2076/77', '2076/77'),
        ('2077/78', '2077/78'),
        ('2078/79', '2078/79'),
        ('2079/80', '2079/80'),
        ('2081/82', '2081/82'),
        ('2082/83', '2082/83')
    )

    QUARTERS = (
        ('Q1', 'Q1'),
        ('Q2', 'Q2'),
        ('Q3', 'Q3'),
        ('Q4', 'Q4')
    )

    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    quarter = models.CharField(null=True, blank=True, max_length=255, choices=QUARTERS)

    planned_start_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    planned_end_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    planned_start_date_AD = models.DateField(null=True, blank=True)
    planned_end_date_AD = models.DateField(null=True, blank=True)
    actual_start_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    actual_end_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    actual_start_date_AD = models.DateField(null=True, blank=True)
    actual_end_date_AD = models.DateField(null=True, blank=True)

    fiscal_year = models.CharField(max_length=255, choices=FISCAL_YEARS)

    estimated_cost = models.PositiveIntegerField(default=0, help_text="In Rs.")
    actual_cost = models.PositiveIntegerField(default=0, help_text="In Rs.", null=True, blank=True)

    responsible_person = models.CharField(null=True, blank=True, max_length=255)

    dss = models.ForeignKey(DSS, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
