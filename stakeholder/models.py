from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Stakeholder(models.Model):
    STAKEHOLDER_TYPE = (
        ('Supplier', 'Supplier'),
        ('Owner', 'Owner'),
        ('Investor', 'Investor'),
        ('Creditor', 'Creditor'),
        ('Community', 'Community'),
        ('Trade Union', 'Trade Union'),
        ('Employer', 'Employer'),
        ('Government Agency', 'Government Agency'),
        ('Customer', 'Customer'),
        ('Media', 'Media'),
        ('None', 'None')
    )
    MINISTRY = (
        ('Ministry of Defence', 'Ministry of Defence'),
        ('Ministry of Home Affairs', 'Ministry of Home Affairs'),
        ('Ministry of Foreign Affairs', 'Ministry of Foreign Affairs'),
        ('Ministry of Federal Affairs & General Administration', 'Ministry of Federal Affairs & General Administration'),
        ('Ministry of Education, Science and Technology', 'Ministry of Education, Science and Technology'),
        ('Ministry of Energy, Water Resources and Irrigation', 'Ministry of Energy, Water Resources and Irrigation'),
        ('Ministry of Agriculture and Livestock Development', 'Ministry of Agriculture and Livestock Development'),
        ('Ministry of Health and Population', 'Ministry of Health and Population'),
        ('Ministry of Industry, Commerce and Supplies', 'Ministry of Industry, Commerce and Supplies'),
        ('Ministry of Culture, Tourism and Civil Aviation', 'Ministry of Culture, Tourism and Civil Aviation'),
        ('Ministry of Forest and Environment', 'Ministry of Forest and Environment'),
        ('Ministry of Labour, Employment and Social Security', 'Ministry of Labour, Employment and Social Security'),
        ('Ministry of Finance', 'Ministry of Finance'),
        ('Ministry of Communication and Information Technology', 'Ministry of Communication and Information Technology'),
        ('Ministry of Youth and Sports', 'Ministry of Youth and Sports'),
        ('Ministry of Land Management, Cooperatives and Poverty Alleviation', 'Ministry of Land Management, Cooperatives and Poverty Alleviation'),
        ('Ministry of Water Supply', 'Ministry of Water Supply'),
        ('Ministry of Physical Infrastructure and Transportation', 'Ministry of Physical Infrastructure and Transportation'),
        ('Ministry of Urban Development', 'Ministry of Urban Development'),
        ('Ministry of Women, Children and Senior Citizen', 'Ministry of Women, Children and Senior Citizen'),
        ('Ministry of Law, Justice and Parliamentary Affairs', 'Ministry of Law, Justice and Parliamentary Affairs'),
        ('None', 'None')
    )

    title = models.CharField(max_length=255)
    description = RichTextField(null=True, blank=True)
    stakeholder_type = models.CharField(max_length=255, choices=STAKEHOLDER_TYPE, default='None')
    ministry = models.CharField(max_length=255, choices=MINISTRY, default='None')

    def __str__(self):
        return self.title

