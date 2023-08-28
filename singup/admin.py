from django.contrib import admin

# Register your models here.
from .models import *

# class SingUPAdmin(admin.ModelAdmin):
#     list_display=('name','email','number','password','date',)

# admin.site.register(singup,SingUPAdmin)

class PaperAdmin(admin.ModelAdmin):
    list_display=('id','user','conference','title_paper','Auth_name','Auth_email','paper_description','paper_upload','start_date','status','reviewer_comments','comment1','comment2','comment3','assigned_reviewers_list')
    list_filter = ('status',)
admin.site.register(paper,PaperAdmin)

class Resubmit_papers_admin(admin.ModelAdmin):
    list_display=('id','paper_id','user','conference','title_paper','Auth_name','paper_description','paper_upload','start_date','status','version','assigned_reviewers_list','reviewer_comments')
    list_filter = ('status',)
admin.site.register(resubmit_papers,Resubmit_papers_admin)

class CustomUserAdmin_by(admin.ModelAdmin):
    list_display=('name','id','email','number','date','is_active','is_staff','is_conference_admin','is_reviewer','is_auth','password')

admin.site.register(CustomUser,CustomUserAdmin_by)
