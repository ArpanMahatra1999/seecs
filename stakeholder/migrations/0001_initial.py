# Generated by Django 3.2.4 on 2021-06-10 04:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('stakeholder_type', models.CharField(choices=[('Supplier', 'Supplier'), ('Owner', 'Owner'), ('Investor', 'Investor'), ('Creditor', 'Creditor'), ('Community', 'Community'), ('Trade Union', 'Trade Union'), ('Employer', 'Employer'), ('Government Agency', 'Government Agency'), ('Customer', 'Customer'), ('Media', 'Media'), ('None', 'None')], default='None', max_length=255)),
                ('ministry', models.CharField(choices=[('Ministry of Defence', 'Ministry of Defence'), ('Ministry of Home Affairs', 'Ministry of Home Affairs'), ('Ministry of Foreign Affairs', 'Ministry of Foreign Affairs'), ('Ministry of Federal Affairs & General Administration', 'Ministry of Federal Affairs & General Administration'), ('Ministry of Education, Science and Technology', 'Ministry of Education, Science and Technology'), ('Ministry of Energy, Water Resources and Irrigation', 'Ministry of Energy, Water Resources and Irrigation'), ('Ministry of Agriculture and Livestock Development', 'Ministry of Agriculture and Livestock Development'), ('Ministry of Health and Population', 'Ministry of Health and Population'), ('Ministry of Industry, Commerce and Supplies', 'Ministry of Industry, Commerce and Supplies'), ('Ministry of Culture, Tourism and Civil Aviation', 'Ministry of Culture, Tourism and Civil Aviation'), ('Ministry of Forest and Environment', 'Ministry of Forest and Environment'), ('Ministry of Labour, Employment and Social Security', 'Ministry of Labour, Employment and Social Security'), ('Ministry of Finance', 'Ministry of Finance'), ('Ministry of Communication and Information Technology', 'Ministry of Communication and Information Technology'), ('Ministry of Youth and Sports', 'Ministry of Youth and Sports'), ('Ministry of Land Management, Cooperatives and Poverty Alleviation', 'Ministry of Land Management, Cooperatives and Poverty Alleviation'), ('Ministry of Water Supply', 'Ministry of Water Supply'), ('Ministry of Physical Infrastructure and Transportation', 'Ministry of Physical Infrastructure and Transportation'), ('Ministry of Urban Development', 'Ministry of Urban Development'), ('Ministry of Women, Children and Senior Citizen', 'Ministry of Women, Children and Senior Citizen'), ('Ministry of Law, Justice and Parliamentary Affairs', 'Ministry of Law, Justice and Parliamentary Affairs'), ('None', 'None')], default='None', max_length=255)),
            ],
        ),
    ]