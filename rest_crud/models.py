from django.db import models

# Create your models here.

class Studentcrud(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()


