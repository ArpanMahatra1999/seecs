# Generated by Django 3.2.4 on 2021-06-10 04:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('type', models.CharField(choices=[('Agriculture', 'Agriculture'), ('Tourism', 'Tourism'), ('Construction', 'Construction')], max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
