from decimal import MAX_EMAX
from django.db import models
from django.forms import CharField

# Create your models here.

class Student_De_serialization(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    roll = models.IntegerField()
