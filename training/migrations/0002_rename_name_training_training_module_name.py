# Generated by Django 3.2.4 on 2021-08-12 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='training',
            old_name='name',
            new_name='training_module_name',
        ),
    ]
