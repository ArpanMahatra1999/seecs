from django.db import models
from django.contrib.auth.models import User
from dss.models import DSS


# Create your models here.
class DSSAdmin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dss = models.ForeignKey(DSS, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " from " + str(self.dss)
