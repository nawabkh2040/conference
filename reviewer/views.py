from django.shortcuts import render , HttpResponse , redirect
from conference import settings
from reviewer.models import Reviewer_data
from django.contrib.auth import authenticate, login , logout
from django.urls import reverse
from reviewer.models import Reviewer_data
from singup.models import CustomUser , paper ,resubmit_papers
from django.core.mail import send_mail
import smtplib
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import * 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import *
from django.shortcuts import get_object_or_404

# Create your views here.


def index(request):
    return render(request,'reviewer/index.html')
    # return HttpResponse("Hello, Reviewer.")

def sing_up_reviewer(request):
    if request.method == "POST":
        full_name=request.POST.get('full-name')
        highest_qualification=request.POST.get('highest-qualification')
        experience=request.POST.get('experience')
        designations=request.POST.get('designations')
        organization=request.POST.get('organization')
        mobile_number=request.POST.get('mobile-number')
        whats_app_number=request.POST.get('whats-app-number')
        email_reviewer=request.POST.get('email_reviewer')
        password_reviewer=request.POST.get('password_reviewer')
        photo_upload = request.FILES.get('photo-upload')
        resume_upload = request.FILES.get('resume-upload')
        print(full_name)
        if Reviewer_data.objects.filter(email=email_reviewer).exists():
                context = {'error_message': 'This email is already registered.'}
                return render(request, 'reviewer/sing-up.html',context)
        if CustomUser.objects.filter(email=email_reviewer).exists():
                context = {'error_message': 'This email is already registered.'}
                return render(request, 'reviewer/sing-up.html',context)
        else:
             new_reviewer=Reviewer_data.objects.create(
                  reviewer_name=full_name,highest_qualification=highest_qualification,experience=experience,designations=designations,organization=organization,reviewer_number=mobile_number,email=email_reviewer,whats_app_number=whats_app_number,password=password_reviewer,photo_upload=photo_upload,resume_upload=resume_upload,
             )
             new_reviewer.save()
             reviewer=CustomUser.objects.create_user(
                  name=full_name,email=email_reviewer,number=mobile_number,password=password_reviewer
             )
             reviewer.is_active = False
             reviewer.is_reviewer = True
             reviewer.save()
             subject2= "Email Verification SDBC Conference"
             from_email =settings.EMAIL_HOST_USER
             to_list = [reviewer.email]
             current_site = get_current_site(request)
             uidb64 = urlsafe_base64_encode(force_bytes(reviewer.id))
             token = default_token_generator.make_token(reviewer)
             context1 = {
                'name': reviewer.name,
                'domain': current_site.domain,
                'uidb64': uidb64,
                'token': token,
                }
             messages2 = render_to_string('reviewer/email_confirmation.html', context1)
             try:
                send_mail(subject2, messages2, from_email, to_list, fail_silently=True)
                context = {'success_message': 'Your Account Create Successfully. Please Check Your Email and Verify It  :-) '}
                return render(request, 'reviewer/sing-up.html', context)
             except smtplib.SMTPException as e:
                print("SMTPException occurred:",e)
                context = {'error_message': 'Your Account Create Successfully. There is a problem to sending mail But You Can login  :-) '}
                return render(request, 'reviewer/sing-up.html', context)
    return render(request,'reviewer/sing-up.html')

def activate_reviewer(request, uidb64, token):
    try:
        uidb64 = force_str(urlsafe_base64_decode(uidb64))
        my_user = CustomUser.objects.get(id=uidb64)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        my_user = None
    if my_user is not None and default_token_generator.check_token(my_user,token):
        my_user.is_active = True
        my_user.save()
        login(request,my_user)
        return redirect('reviewer-dashboard')
    else:
   
        return render(request,'reviewer/activation-failed.html')

def sing_in_reviewer(request):
    if request.user.is_authenticated:
         return redirect('reviewer-dashboard')
    if request.method == 'POST':
         email=request.POST.get('email')
         password=request.POST.get('password')
         print(email)
         print(password)
         user=authenticate(request,email=email,password=password)
         print(user)
         if user is not None:
            #   login(request, user)
            #   print(request.user.is_authenticated)
            #   print(user.reviewer_name)
            #   return redirect('reviewer-dashboard')
            login(request,user)
            return redirect('reviewer-dashboard')
         else:
              context={
                   'error_message': 'Invalid Email or Password.'
              }
              return render(request,'reviewer/sing-in.html',context)
    return render(request,'reviewer/sing-in.html')



def dashboard_reviewer(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated: 
        user=request.user
        fname=user.name
        if user.is_reviewer:
            try:
                reviewer=Reviewer_data.objects.get(email=user)
            except Exception as e:
                print(e)
                logout(request)
                return redirect('reviewer-sing-in')
            add_id_ok=user.id
            reviewer.reviewer_id=add_id_ok
            reviewer.save()
            if reviewer.is_ok:
                reviewer_instance = get_object_or_404(Reviewer_data, email=user.email)
                papers = paper.objects.filter(assigned_reviewers=reviewer_instance)
                fname=reviewer.reviewer_name
                reviewer=reviewer
                content ={
                'reviewer':reviewer,
                'papers':papers,
                }
                return render(request,'reviewer/dashboard.html',content)
            else:
                content ={
                    "user":user,
                    "fname":fname,
                    "message_error":"You Are Not Verify By Admin Wait or Contact With Admin"
                }
                return render(request,'reviewer/dashboard.html',content)
        else:
            print("User is ",fname,"Not Reviewer")
            logout(request)
            return redirect('reviewer-sing-in')
    else :
        return redirect('reviewer-sing-in')
    
def sing_out_reviewer(request):
    logout(request)
    return redirect('reviewer-sing-in')

def list_of_submitted_papers(request):
    if request.user.is_authenticated: 
        user=request.user
        fname=user.name
        if user.is_reviewer:
            add_id=Reviewer_data.objects.get(email=user)
            add_id_ok=user.id
            add_id.reviewer_id=add_id_ok
            add_id.save()
            if add_id.is_ok:
                reviewer_instance = get_object_or_404(Reviewer_data, email=user.email)
                papers = paper.objects.filter(assigned_reviewers=reviewer_instance)
                fname=add_id.reviewer_name
                content ={
                "add_id":add_id,
                "papers" : papers,
                }
                return render(request,'reviewer/submitted_paper.html',content)
            else:
                content ={
                    "user":user,
                    "fname":fname,
                    "message_error":"You Are Not Verify By Admin Wait or Contact With Admin"
                }
                return render(request,'reviewer/dashboard.html',content)
        else:
            print("User is ",fname,"Not Reviewer")
            logout(request)
            return redirect('reviewer-sing-in')
    else :
        return redirect('reviewer-sing-in')
    
def list_of_resubmitted_papers(request):
    if request.user.is_authenticated: 
        user=request.user
        fname=user.name
        if user.is_reviewer:
            add_id=Reviewer_data.objects.get(email=user)
            add_id_ok=user.id
            add_id.reviewer_id=add_id_ok
            add_id.save()
            if add_id.is_ok:
                reviewer_instance = get_object_or_404(Reviewer_data, email=user.email)
                papers = resubmit_papers.objects.filter(assigned_reviewers=reviewer_instance)
                fname=add_id.reviewer_name
                content ={
                "add_id":add_id,
                "papers" : papers,
                }
                return render(request,'reviewer/resubmitted_paper.html',content)
            else:
                content ={
                    "user":user,
                    "fname":fname,
                    "message_error":"You Are Not Verify By Admin Wait or Contact With Admin"
                }
                return render(request,'reviewer/dashboard.html',content)
        else:
            print("User is ",fname,"Not Reviewer")
            logout(request)
            return redirect('reviewer-sing-in')
    else :
        return redirect('reviewer-sing-in')
    
def paper_reviewer(request, paper_id):
    if request.user.is_authenticated and request.user.is_reviewer:
        try:
            paper_instance = paper.objects.get(id=paper_id)
        except paper.DoesNotExist:
            return HttpResponse("Unknown Paper Id") # Handle the case when paper doesn't exist

        if request.method == 'POST':
            comment = request.POST.get('comment')
            print("Review Submitted Comment : ",comment)
            paper_instance.reviewer_comments[request.user.id] = comment
            paper_instance.save()

        context = {
            "paper": paper_instance,
        }
        return render(request, 'reviewer/review_paper.html', context)

    else:
        return redirect('reviewer-sign-in')

def paper_reviewer_resubmit(request, paper_id):
    if request.user.is_authenticated and request.user.is_reviewer:
        try:
            paper_instance = resubmit_papers.objects.get(id=paper_id)
        except paper.DoesNotExist:
            return HttpResponse("Unknown Paper Id") # Handle the case when paper doesn't exist

        if request.method == 'POST':
            comment = request.POST.get('comment')
            print("Review ReSubmitted Comment : ",comment)
            paper_instance.reviewer_comments[request.user.id] = comment
            paper_instance.save()

        context = {
            "paper": paper_instance,
        }
        return render(request, 'reviewer/review_resubmit_paper.html', context)

    else:
        return redirect('reviewer-sign-in')

def reviewer_profile(request, reviewer_id):
    if request.user.is_authenticated and request.user.is_reviewer:
        reviewer_instance=Reviewer_data.objects.get(id=reviewer_id)   
        context={
            "reviewer" : reviewer_instance,
        }    
        return render(request,'reviewer/reviewer_profile.html',context)
    else:
        return redirect('reviewer-sign-in')