# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    activated = models.BooleanField(default=False)
    authorisation = models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    karma = models.IntegerField(default=0)


class Person(User):
    profile_data = Profile()
    class Meta:
        proxy = True



