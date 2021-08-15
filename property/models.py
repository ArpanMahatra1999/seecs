from ckeditor.fields import RichTextField

from django.contrib.auth.models import User
from django.db import models
from nepali_datetime_field.models import NepaliDateField

from dss.models import DSS


# Create your models here.
class Property(models.Model):

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
    PROPERTY_TYPES = (
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

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_purchase_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_purchase_AD = models.DateField(null=True, blank=True)

    property_type = models.CharField(max_length=255, choices=PROPERTY_TYPES)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=255, choices=UNITS, null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.title)
