from django.db import models

# Create your models here.

class emp(models.Model):
    eno=models.CharField(max_length=30)
    ename=models.CharField(max_length=30)