from django.db import models
from django.forms import DateTimeField
from django.utils import timezone

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=50)
    email=models.CharField(max_length=120,unique='True')
    password=models.CharField(max_length=120)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
          return self.username
class conference(models.Model):
     conference_name = models.CharField(max_length=80)
     conference_descriptions = models.CharField(max_length=600)
     conference_start_date = models.DateTimeField(default=timezone.now)
     conference_end_date = models.DateField()
     has_uploaded_paper = models.BooleanField(default=False)
     def __str__(self):
          return self.conference_name
     