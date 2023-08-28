# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# from django.db import models

# from datetime import timezone
# from django.utils import *
# from django.contrib.auth.models import * 





# class CustomUserManager(BaseUserManager):
#      def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
        
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#      def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)

#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')

#         return self.create_user(email, password, **extra_fields)

# class CustomUser(AbstractBaseUser,PermissionsMixin):
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=('groups'),
#         blank=True,
#         related_name='customuser_set',  # Add a related_name
#         related_query_name='user'
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=('user permissions'),
#         blank=True,
#         related_name='customuser_set',  # Add a related_name
#         related_query_name='user'
#     )
#     name = models.CharField(max_length=70)
#     email = models.EmailField(unique=True)
#     number = models.CharField(max_length=15)
#     password = models.CharField(max_length=500)
#     date = models.DateTimeField(default=timezone.now)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_reviewer = models.BooleanField(default=False)
#     objects = CustomUserManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name', 'number']
#     def __str__(self):
#         return self.email
#     username = models.CharField(max_length=70, null=True, blank=True)