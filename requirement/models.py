from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from activity.models import Activity
from dss.models import DSS


# Create your models here.
class Requirement(models.Model):

    UNITS = (
        ('Pieces', 'Pieces'),
        ('Unit', 'Unit'),
        ('Boxes', 'Boxes'),
        ('Cartoon', 'Cartoon'),
        ('Meter', 'Meter'),
        ('Cubic Meter', 'Cubic Meter'),
        ('sq.m', 'sq.m'),
        ('sq.KM', 'sq.KM'),
        ('Acres', 'Acres'),
        ('Hectares', 'Hectares'),
        ('Paisa', 'Paisa'),
        ('Aana', 'Aana'),
        ('Ropani', 'Ropani'),
        ('Dhur', 'Dhur'),
        ('Kattha', 'Kattha'),
        ('Bigha', 'Bigha')
    )
    TYPES = (
        ('Land', 'Land'),
        ('Building', 'Building'),
        ('Furniture', 'Furniture'),
        ('Automobile', 'Automobile'),
        ('Electronic', 'Electronic'),
        ('Others', 'Others')
    )
    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)

    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True, blank=True)

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    estimated_date_of_purchase_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    estimated_date_of_purchase_AD = models.DateField(null=True, blank=True)

    requirement_type = models.CharField(max_length=255, choices=TYPES)
    unit = models.CharField(max_length=255, choices=UNITS, null=True, blank=True)
    estimated_quantity = models.PositiveIntegerField(default=0)
    estimated_price = models.PositiveIntegerField(default=0, help_text="In Rupees")
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)
