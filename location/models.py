from django.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name)


class District(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class Municipality(models.Model):
    name = models.CharField(max_length=255)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)
