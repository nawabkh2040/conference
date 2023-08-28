from django.db import models
from django.forms import DateTimeField
from django.utils import timezone
# from singup.models import CustomUser

# Create your models here.
# class Login(models.Model):
#     username = models.CharField(max_length=50)
#     email=models.CharField(max_length=120,unique='True')
#     password=models.CharField(max_length=120)
#     date = models.DateTimeField(default=timezone.now)
#     def __str__(self):
#           return self.username
class conference(models.Model):
     conference_name = models.CharField(max_length=80)
     conference_descriptions = models.CharField(max_length=600)
     conference_start_date = models.DateTimeField(default=timezone.now)
     conference_end_date = models.DateField()
     conference_venue=models.CharField(max_length=250,default="online",null=True)
     STATUS_CHOICES = (
        ('online', 'Online'),
        ('offline', 'Offline'),
        ('hybrid', 'Hybrid'),
        )
     conference_mode= models.CharField(max_length=20, choices=STATUS_CHOICES, default='online')

     conference_user = models.CharField(default="Not present",max_length=150)
     
     has_uploaded_paper = models.BooleanField(default=False)
     
     def __str__(self):
          return self.conference_name
     