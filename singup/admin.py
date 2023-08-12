from django.contrib import admin

# Register your models here.
from .models import *

# class SingUPAdmin(admin.ModelAdmin):
#     list_display=('name','email','number','password','date',)

# admin.site.register(singup,SingUPAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display=('id','user','conference','title_paper','Auth_name','paper_description','paper_upload','start_date','expiry_date','status','has_uploaded_paper')
    list_filter = ('status',)
admin.site.register(paper,PaperAdmin)

class CustomUserAdmin_by(admin.ModelAdmin):
    list_display=('name','email','number','password','date','is_active','is_staff')

admin.site.register(CustomUser,CustomUserAdmin_by)
