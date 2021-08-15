from django.db import models
from django.contrib.auth.models import User
from nepali_datetime_field.models import NepaliDateField

from dss.models import DSS
from course.models import Course
from stakeholder.models import Stakeholder
from trainer.models import Trainer
from location.models import Province, District, Municipality


# Create your models here.
class CourseClass(models.Model):
    HOURS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
    )
    SHIFTS = (
        ('Morning', 'Morning'),
        ('Day', 'Day'),
    )
    DAYS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    )
    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    trainers = models.ManyToManyField(Trainer, help_text="Use Ctrl to select multiple trainers")

    coordinator = models.TextField(null=True, blank=True)
    assistant_trainer = models.TextField(null=True, blank=True)
    venue = models.TextField(null=True, blank=True)

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_starting_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_ending_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_starting_AD = models.DateField(null=True, blank=True)
    date_of_ending_AD = models.DateField(null=True, blank=True)

    shift = models.CharField(max_length=255, choices=SHIFTS, null=True, blank=True)
    average_hours_per_day = models.IntegerField(choices=HOURS, null=True, blank=True)
    days_per_week = models.IntegerField(choices=DAYS, null=True, blank=True, default=6)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course) + " on " + str(self.dss)


class Test(models.Model):

    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    registration_number = models.TextField()
    symbol_number = models.CharField(max_length=255, null=True, blank=True)

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_application_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_exam_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_result_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    date_of_application_AD = models.DateField(null=True, blank=True)
    date_of_exam_AD = models.DateField(null=True, blank=True)
    date_of_result_AD = models.DateField(null=True, blank=True)

    result_status = models.CharField(max_length=255, null=True, blank=True)
    remark = models.CharField(max_length=255, null=True, blank=True)
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE)
    trainee = models.ForeignKey('trainee.Trainee', on_delete=models.CASCADE)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.trainee.first_name) + " " + str(self.trainee.last_name) + " on " + str(self.course_class)


class Employment(models.Model):

    STATUS = (
        ('Own a business', 'Own a business'),
        ('Employed & Course related', 'Employed & Course related'),
        ('Employed & Course unrelated', 'Employed & Course unrelated'),
        ('Unemployed', 'Unemployed'),
    )
    CALENDAR = (
        ('BS', 'BS'),
        ('AD', 'AD')
    )

    calendar = models.CharField(max_length=255, choices=CALENDAR)

    date_of_call_BS = NepaliDateField(null=True, blank=True)
    date_of_call_AD = models.DateField(null=True, blank=True)

    job_status = models.CharField(max_length=100, choices=STATUS, default='Unemployed')
    description = models.TextField(null=True, blank=True)
    course_class = models.ForeignKey(CourseClass, on_delete=models.CASCADE)
    employer = models.ForeignKey(Stakeholder, on_delete=models.SET_NULL, null=True, blank=True)
    office = models.CharField(max_length=255, null=True, blank=True, help_text="Write Office name if it isn't among above employers")

    start_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    end_date_BS = NepaliDateField(null=True, blank=True, help_text="Write in YYYY-MM-DD format")
    start_date_AD = models.DateField(null=True, blank=True)
    end_date_AD = models.DateField(null=True, blank=True)

    office_province = models.ForeignKey(Province, on_delete=models.CASCADE)
    office_district = models.ForeignKey(District, on_delete=models.CASCADE)
    office_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE)
    salary = models.PositiveIntegerField(help_text="Please mention the salary in Rs.", null=True, blank=True)
    trainee = models.ForeignKey('trainee.Trainee', on_delete=models.CASCADE)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.trainee.first_name) + " " + str(self.trainee.last_name) + " on " + str(self.course_class)

