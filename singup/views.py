from base64 import urlsafe_b64decode, urlsafe_b64encode
from collections import UserDict, UserList
from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from .models import  CustomUser,CustomUserManager , paper ,resubmit_papers
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# from .backends import CustomBackend
from django.contrib import messages
import smtplib
import pandas as pd
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import * 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import *
from django.shortcuts import render, get_object_or_404, redirect


def download_papers_excel(request):
    papers = paper.objects.all()  # Fetch all paper objects

    # Create a DataFrame to hold the data
    data = {
        'Paper Id': [paper.id for paper in papers],
        'Paper Title': [paper.title_paper for paper in papers],
        'Paper Version': [f'v{paper.version}' for paper in papers],
        'Auth Name': [paper.Auth_name for paper in papers],
        'Conference Name': [paper.conference for paper in papers],
        'User Email': [paper.user for paper in papers],
        'Paper Description': [paper.paper_description for paper in papers],
        'Paper Upload': [paper.paper_upload.url for paper in papers],
        'Date Of Submit': [paper.start_date for paper in papers],
    }

    df = pd.DataFrame(data)

    # Create an Excel writer
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=papers.xlsx'
    writer = pd.ExcelWriter(response, engine='xlsxwriter')

    # Convert the DataFrame to an XlsxWriter Excel object
    df.to_excel(writer, sheet_name='Papers', index=False)

    # Close the Pandas Excel writer and output the Excel file to the response
    writer.save()

    return response



def singup_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        password = request.POST.get('password')
        # print(email, name)
        if CustomUser.objects.filter(email=email).exists():
                context = {'error_message': 'This email is already registered.'}
                return render(request, 'singup/singup.html',context)        
        else:
            my_user = CustomUser.objects.create_user(
                    name=name,
                    email=email,
                    number=number,
                    password=password,
                )
            my_user.is_active = False
            my_user.save()
            # welcome Email Function
            # subject = "WELCOME TO SDBC CONFERENCE"
            subject2= "Email Verification SDBC Conference"
            # messages = "Hello "+my_user.name+"  !!\n"+"Welcome to SDBC Conference \n"+"Your Account is under the Verification Process .\n"+"You Get A Another Mail & It Content the verification link. You Have to Click it. Then Your Account will Activated :-)  "
            from_email =settings.EMAIL_HOST_USER
            to_list = [my_user.email]
            # send_mail(subject, messages, from_email, to_list, fail_silently=True)
            # Confirmation Email
            current_site = get_current_site(request)
            uidb64 = urlsafe_base64_encode(force_bytes(my_user.id))
            token = default_token_generator.make_token(my_user)
            context1 = {
                'name': my_user.name,
                'domain': current_site.domain,
                'uidb64': uidb64,
                'token': token,
                }
            messages2 = render_to_string('singup/email_confirmation.html', context1)
            try:
                send_mail(subject2, messages2, from_email, to_list, fail_silently=True)
                context_success = {'success_message': 'Your Account Create Successfully. Please Check Your Email and Verify It  :-) '}
                return render(request, 'singup/singIn.html', context_success)
            except smtplib.SMTPException as e:
                print("SMTPException occurred:",e)
                context_success = {'error_message': 'Your Account Create Successfully. There is a problem to sending mail But You Can login  :-) '}
                return render(request, 'singup/singIn.html', context_success)
    else:
        return render(request, 'singup/singup.html')
def singIn(request):
    if request.user.is_authenticated:
        return redirect('success')
    if request.method=="POST":
        get_email=request.POST['email']
        get_password=request.POST["password"]
        # hashed_password = make_password(get_password)
        print("Email is",get_email)
        print("Password is ",get_password)
        # print("Hashed Password is --- ",hashed_password)
        user = authenticate(request,email=get_email,password=get_password)
        print("User singIn is----",user)
        if user is not None:
            login(request,user)
            return redirect('success')
        else:
            context = {'error_message': 'Invalid email or password'}
            return render(request, 'singup/singIn.html', context)
    else:
        return render(request, 'singup/singIn.html')
def logout_page(request):
    logout(request)
    return redirect('/')
def success_view(request):
    # Your view logic here
    # if User is authenticated:
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        user=request.user
        print("User is ",user.name)
        context={
            'conference':conference.objects.all(),
            'uname' : user.name,
        }
        return render(request, 'singup/dashboard.html',context)
    else:
        return redirect('singin') 
def activate(request, uidb64, token):
    try:
        uidb64 = force_str(urlsafe_base64_decode(uidb64))
        my_user = CustomUser.objects.get(id=uidb64)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        my_user = None
    if my_user is not None and default_token_generator.check_token(my_user,token):
        my_user.is_active = True
        my_user.save()
        login(request,my_user)
        return redirect('success')
    else:
   
        return render(request,'singup/activation-failed.html')
"""

def resubmit(request, conf_id):
    if request.user.is_authenticated:
        conf_instance = get_object_or_404(conference, id=conf_id)
        conf_ins= conference.objects.all()
        # int(conf_instance)
        conf= conference.objects.get(conference_name=conf_instance)
        v1=conf_instance.id
        if conf is not None:
            print(conf)
        print(conf_instance)
        user=request.user
        print("User is ",user.name)
        if request.method=="POST":
            int(conf_instance.id)
            user=request.user
            # conf = request.POST.get('conference_id')
            title_paper = request.POST.get('title_paper')
            Auth_paper = request.POST.get('Auth_paper')
            Description = request.POST.get('Description')
            pdf_upload = request.FILES.get('pdf_upload')
            expiry_date = request.POST.get('expiry_date')
            # print(conf)
            print(title_paper)
            print(Auth_paper)
            print(Description)
            print(pdf_upload)
            print(expiry_date)
            new_paper = paper.objects.create(
                title_paper=title_paper, 
                Auth_name=Auth_paper, 
                paper_description=Description,   
                paper_upload=pdf_upload, 
                expiry_date=expiry_date, 
                user=user, 
                status='pending',
                conference=conf_instance,
            )
            conf_instance.has_uploaded_paper = True
            new_paper.save()
            context = {
                'error_message': 'Successfully Upload Your Paper',
                'v1':conf_instance.id,
                }
            print(v1)
            return render(request, 'singup/upload.html',context)
        
        context ={
            'v1':conf_instance.id,
            'uname' : user.name,
        }
        return render(request, 'singup/upload.html',context)
    else:
        return render(request, 'singup/singIn.html')

"""
def re_resubmit(request,re_paper_id):
    if request.user.is_authenticated:
        user = request.user
        original_paper = get_object_or_404(resubmit_papers, id=re_paper_id)
        if request.method=="POST":
            paper_title=request.POST.get('title_paper')
            Auth_name=request.POST.get('Auth_name')
            paper_keyword=request.POST.get('paper_keyword')
            paper_description=request.POST.get('paper_description')
            pdf_upload = request.FILES.get('pdf_upload')
            print(original_paper)
            re_resubmit_paper=resubmit_papers(
                paper_id=original_paper.paper_id,
                user=original_paper.user,
                status='pending',
                paper_keyword=paper_keyword,
                conference=original_paper.conference,
                title_paper=paper_title,
                Auth_name=Auth_name,
                paper_description=paper_description,
                paper_upload=pdf_upload,
                Auth_affiliation=original_paper.Auth_affiliation,
                Auth_email=original_paper.Auth_email,
                Auth_mobile=original_paper.Auth_mobile,
                corresponding_auth_name=original_paper.corresponding_auth_name,
                corresponding_auth_email=original_paper.corresponding_auth_email,
                corresponding_auth_mobile=original_paper.corresponding_auth_mobile,
                corresponding_auth_affiliation=original_paper.corresponding_auth_affiliation,
                other_auth_mobile=original_paper.other_auth_mobile,
                other_auth_email=original_paper.other_auth_email,
                other_auth_name=original_paper.other_auth_name,
                other_auth_affiliation=original_paper.other_auth_affiliation,
                version=original_paper.version + 1

            )
            re_resubmit_paper.save()
            context = {
                'error_message': 'Successfully Upload Your Paper',
                "original_paper":get_object_or_404(resubmit_papers, id=re_paper_id),
                "fname":user.name,
                }
            return render(request, 'singup/resubmit.html',context)
            
        context={
            "original_paper":get_object_or_404(resubmit_papers, id=re_paper_id),
            "user":request.user,
            "fname":user.name,
        }
        return render(request,'singup/re_resubmit.html',context)

def resubmit(request,paper_id):
    if request.user.is_authenticated:
        user = request.user
        original_paper = get_object_or_404(paper, id=paper_id)
        if request.method=="POST":
            paper_title=request.POST.get('title_paper')
            Auth_name=request.POST.get('Auth_name')
            paper_keyword=request.POST.get('paper_keyword')
            paper_description=request.POST.get('paper_description')
            pdf_upload = request.FILES.get('pdf_upload')
            print(paper_keyword)
            resubmit_paper=resubmit_papers(
                paper_id=original_paper.id,
                user=original_paper.user,
                status='pending',
                paper_keyword=paper_keyword,
                conference=original_paper.conference,
                title_paper=paper_title,
                Auth_name=Auth_name,
                paper_description=paper_description,
                paper_upload=pdf_upload,
                Auth_affiliation=original_paper.Auth_affiliation,
                Auth_email=original_paper.Auth_email,
                Auth_mobile=original_paper.Auth_mobile,
                corresponding_auth_name=original_paper.corresponding_auth_name,
                corresponding_auth_email=original_paper.corresponding_auth_email,
                corresponding_auth_mobile=original_paper.corresponding_auth_mobile,
                corresponding_auth_affiliation=original_paper.corresponding_auth_affiliation,
                other_auth_mobile=original_paper.other_auth_mobile,
                other_auth_email=original_paper.other_auth_email,
                other_auth_name=original_paper.other_auth_name,
                other_auth_affiliation=original_paper.other_auth_affiliation,
                version=original_paper.version + 1

            )
            resubmit_paper.save()
            context = {
                'error_message': 'Successfully Upload Your Paper',
                "original_paper":get_object_or_404(paper, id=paper_id),
                "fname":user.name,
                }
            return render(request, 'singup/resubmit.html',context)
            
        context={
            "original_paper":get_object_or_404(paper, id=paper_id),
            "user":request.user,
            "fname":user.name,
        }
        return render(request,'singup/resubmit.html',context)

def submit_paper(request,conf_id):
    if request.user.is_authenticated:
        user = request.user
        conf_instance = get_object_or_404(conference, id=conf_id)
        if request.method=="POST":
            user=request.user
            title_paper=request.POST.get('title_paper')
            Auth_name=request.POST.get('Auth_name')
            Auth_email=request.POST.get('Auth_email')
            Auth_affiliation=request.POST.get('Auth_affiliation')
            Auth_mobile=request.POST.get('Auth_mobile')
            corresponding_auth_name=request.POST.get('corresponding_auth_name')
            corresponding_auth_email=request.POST.get('corresponding_auth_email')
            corresponding_auth_affiliation=request.POST.get('corresponding_auth_affiliation')
            corresponding_auth_mobile=request.POST.get('corresponding_auth_mobile')
            other_auth_name=request.POST.get('other_auth_name')
            other_auth_email=request.POST.get('other_auth_email')
            other_auth_affiliation=request.POST.get('other_auth_affiliation')
            other_auth_mobile=request.POST.get('other_auth_mobile')
            paper_keyword=request.POST.get('paper_keyword')
            paper_description=request.POST.get('paper_description')
            pdf_upload = request.FILES.get('pdf_upload')
            print(pdf_upload)
            new_paper=paper.objects.create(
                user=user,
                title_paper=title_paper,
                Auth_name=Auth_name,
                Auth_email=Auth_email,
                Auth_affiliation=Auth_affiliation,
                Auth_mobile=Auth_mobile,
                corresponding_auth_name=corresponding_auth_name,
                corresponding_auth_email=corresponding_auth_email,
                corresponding_auth_affiliation=corresponding_auth_affiliation,
                corresponding_auth_mobile=corresponding_auth_mobile,
                other_auth_name=other_auth_name,
                other_auth_email=other_auth_email,
                other_auth_affiliation=other_auth_affiliation,
                other_auth_mobile=other_auth_mobile,
                paper_keyword=paper_keyword,
                paper_description=paper_description,
                paper_upload=pdf_upload,
                status='pending',
                conference=conf_instance,
            )
            conf_instance.has_uploaded_paper = True
            new_paper.save()
            context = {
                'error_message': 'Successfully Upload Your Paper',
                'v1':conf_instance.id,
                }
            return render(request, 'singup/first_upload.html',context)
        else:
            context ={
                'v1':conf_instance.id,
                'uname' : user.name,
            }
            return render(request, 'singup/first_upload.html',context)
    else:
        return redirect('signIn')


def list_of_paper(request,conf_id):
    if request.user.is_authenticated:
        user = request.user
        context={
            'papers_uploaded':paper.objects.filter(user=user,conference_id=conf_id),
            'reupload_paper':resubmit_papers.objects.filter(user=user,conference_id=conf_id),
        }
        return render(request, 'singup/list_of_paper.html',context)
    else:
        return render(request, 'singup/singIn.html')



def list_of_conference(request):
    from login.models import conference
    # conference = conference.objects.all()
    if request.user.is_authenticated:
        conference = conference.objects.all()
        user = request.user
        print("He Check The Conference List",user.name)
        return render(request,"singup/list_of_conference.html",{'conference':conference})
    else:
        return render(request, 'singup/singIn.html')



def conference_detail(request, conf_id):
    if request.user.is_authenticated:
        conf_instance = get_object_or_404(conference, id=conf_id)
        user=request.user
        print(conf_instance.has_uploaded_paper)
        context={
            'conf_instance': conf_instance,
            'papers_uploaded' : paper.objects.filter(user=user, conference=conf_instance),
        }
        return render(request, 'singup/conference_detail.html', context)
    else:
        return render(request, 'singup/singIn.html')
