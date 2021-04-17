from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
from django.utils.timezone import now

class Dyno(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    test = models.CharField(max_length=100)
    constant = models.BooleanField(default=True)
    throttle = models.IntegerField()
    rpm = models.IntegerField()
    