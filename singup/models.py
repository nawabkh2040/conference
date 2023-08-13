from django.db import models
from datetime import timezone
from django.utils import *
from django.contrib.auth.models import * 
from login.models import conference
from login.models import conference


class CustomUserManager(BaseUserManager):
     def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
     def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser,PermissionsMixin):
    name = models.CharField(max_length=70)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=15)
    password = models.CharField(max_length=500)
    date = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'number']
    def __str__(self):
        return self.email
    username = models.CharField(max_length=70, null=True, blank=True)
     
class paper(models.Model):
     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=None)
     title_paper=models.CharField(max_length=70)
     Auth_name=models.CharField(max_length=70)
     paper_description=models.CharField(max_length=500)
     paper_upload=models.FileField(upload_to='papers/')
     start_date=models.DateTimeField(default=timezone.now)
    #  expiry_date=models.CharField(max_length=20)
     STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        )
     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
     has_uploaded_paper = models.BooleanField(default=False)
     conference = models.ForeignKey(
        conference,
        on_delete=models.CASCADE,
        default=None,
        null=True,
        related_name='papers'
    )
     Auth_email = models.EmailField(default='example@example.com')
     Auth_affiliation = models.CharField(max_length=100, default='No affiliation')
     Auth_mobile = models.CharField(max_length=20, default='N/A')
     corresponding_auth_name = models.CharField(max_length=100, default='Unknown')
     corresponding_auth_email = models.EmailField(default='corresponding@example.com')
     corresponding_auth_affiliation = models.CharField(max_length=100, default='No affiliation')
     corresponding_auth_mobile = models.CharField(max_length=20, default='N/A')
     other_auth_name = models.CharField(max_length=100, default='Unknown')
     other_auth_email = models.CharField(max_length=150,default='other@example.com')
     other_auth_affiliation = models.CharField(max_length=100, default='No affiliation')
     other_auth_mobile = models.CharField(max_length=20, default='N/A')
     paper_keyword = models.CharField(max_length=100, default='No keywords')
    

     def __str__(self):
          return self.title_paper


