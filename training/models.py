from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from dss.models import DSS


# Create your models here.
class Training(models.Model):

    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    training_module_name = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    planned_start_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    planned_end_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    actual_start_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    actual_end_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    planned_start_date_AD = models.DateField(null=True, blank=True)
    planned_end_date_AD = models.DateField(null=True, blank=True)
    actual_start_date_AD = models.DateField(null=True, blank=True)
    actual_end_date_AD = models.DateField(null=True, blank=True)

    proposed_training_providing_agencies = models.CharField(max_length=255, null=True, blank=True, help_text="Separate agencies name by commas.")
    number_of_attendees = models.PositiveIntegerField(default=0)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Capacity Building'

    def __str__(self):
        return str(self.training_module_name)
