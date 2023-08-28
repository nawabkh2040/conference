from django.contrib import admin
from .models import *

# Register your models here.

class Reviewer_admin(admin.ModelAdmin):
    list_display=('reviewer_name','id','reviewer_id','highest_qualification','experience','designations','organization','email','reviewer_number','whats_app_number','password','date_reviewer','photo_upload','resume_upload','is_active','is_ok','is_staff')

admin.site.register(Reviewer_data,Reviewer_admin)