from django.db import models

# Create your models here.

class StudentTokenAuthenticationModel(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    roll = models.IntegerField()


##### CREATE TOKEN WITH SIGNAL
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=None, **kwargs):
    if created:
        Token.objects.create(user=instance)











