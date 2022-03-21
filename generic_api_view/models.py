from django.db import models

# Create your models here.
class StudentGenericModel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()

class StudentGenericApiModel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()