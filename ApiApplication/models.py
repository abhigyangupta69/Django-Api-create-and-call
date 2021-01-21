from dateutil.utils import today
from django.db import models
from datetime import datetime
# Create your models here.
##############Create Api using APiView#############
from django.utils import timezone


class Book(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)

##############Create Api using ModelViewSet#############
class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    dob=models.DateField(default=timezone.now())

