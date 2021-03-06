# Generated by Django 3.2.4 on 2021-08-12 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0002_rename_targeted_budget_activity_estimated_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='quarter',
            field=models.CharField(blank=True, choices=[('Q1', 'Q1'), ('Q2', 'Q2'), ('Q3', 'Q3'), ('Q4', 'Q4')], max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
