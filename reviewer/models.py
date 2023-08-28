from django.db import models
# from singup.models import CustomUserManager
from django.utils import *
from django.contrib.auth.models import *
# from conference.settings import TIME_ZONE 
from django.utils import timezone


# Create your models here.

class Reviewer_data(AbstractBaseUser,PermissionsMixin):
    groups = models.ManyToManyField(
        Group,
        verbose_name=('groups'),
        blank=True,
        related_name='reviewerdata_set',  # Add a related_name
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        related_name='reviewerdata_set',  # Add a related_name
        related_query_name='user'
    )
    reviewer_id = models.IntegerField(default=0)
    reviewer_name = models.CharField(max_length=70)
    highest_qualification = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    designations = models.CharField(max_length=70)
    organization = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    reviewer_number = models.CharField(max_length=15)
    whats_app_number = models.CharField(max_length=15)
    password = models.CharField(max_length=250)
    date_reviewer = models.DateTimeField(default=timezone.now)
    photo_upload=models.FileField(upload_to='reviewer/profile-photos/')
    resume_upload=models.FileField(upload_to='reviewer/profile-resume/')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_ok = models.BooleanField(default=False)

    # objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['reviewer_name', 'reviewer_number']
    def __str__(self):
        return self.email