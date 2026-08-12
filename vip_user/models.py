from django.db import models

# Create your models here.
class VipUser(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    age = models.IntegerField()
    phone = models.CharField(max_length=11 , null=True)