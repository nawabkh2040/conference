from django.contrib import admin
from login.models import *

# Register your models here.
# admin.site.register(Login)

class Conference_Admin(admin.ModelAdmin):
    list_display = ('id','conference_name','conference_user','conference_descriptions','conference_start_date','conference_end_date','has_uploaded_paper','conference_mode','conference_venue')


admin.site.register(conference,Conference_Admin)