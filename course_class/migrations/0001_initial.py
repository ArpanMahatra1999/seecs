# Generated by Django 3.2.4 on 2021-06-10 04:05

from django.db import migrations, models
import django.db.models.deletion
import nepali_datetime_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dss', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.CharField(choices=[('BS', 'BS'), ('AD', 'AD')], max_length=255)),
                ('date_of_starting_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('date_of_ending_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('date_of_starting_AD', models.DateField(blank=True, null=True)),
                ('date_of_ending_AD', models.DateField(blank=True, null=True)),
                ('shift', models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Day', 'Day')], max_length=255, null=True)),
                ('average_hours_per_day', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], null=True)),
                ('days_per_week', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendar', models.CharField(choices=[('BS', 'BS'), ('AD', 'AD')], max_length=255)),
                ('date_of_call_BS', nepali_datetime_field.models.NepaliDateField(blank=True, null=True)),
                ('date_of_call_AD', models.DateField(blank=True, null=True)),
                ('job_status', models.CharField(choices=[('Own a business', 'Own a business'), ('Employed & Course related', 'Employed & Course related'), ('Employed & Course unrelated', 'Employed & Course unrelated'), ('Unemployed', 'Unemployed')], default='Unemployed', max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('office', models.CharField(blank=True, help_text="Write Office name if it isn't among above employers", max_length=255, null=True)),
                ('start_date_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('end_date_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('start_date_AD', models.DateField(blank=True, null=True)),
                ('end_date_AD', models.DateField(blank=True, null=True)),
                ('salary', models.PositiveIntegerField(blank=True, help_text='Please mention the salary in Rs.', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.TextField()),
                ('calendar', models.CharField(choices=[('BS', 'BS'), ('AD', 'AD')], max_length=255)),
                ('date_of_application_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('date_of_exam_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('date_of_result_BS', nepali_datetime_field.models.NepaliDateField(blank=True, help_text='Write in YYYY-MM-DD format', null=True)),
                ('date_of_application_AD', models.DateField(blank=True, null=True)),
                ('date_of_exam_AD', models.DateField(blank=True, null=True)),
                ('date_of_result_AD', models.DateField(blank=True, null=True)),
                ('result_status', models.CharField(blank=True, max_length=255, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('course_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_class.courseclass')),
                ('dss', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dss.dss')),
            ],
        ),
    ]