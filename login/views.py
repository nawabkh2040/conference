from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import *
from .models import *
from singup.models import  CustomUser,CustomUserManager
from django.contrib.auth import get_user_model 
from django.contrib.auth.decorators import login_required
from singup.models import paper
from django.contrib.auth import authenticate, login , logout 
from login.models import conference
# Create your views here ....
# @login_required(login_url='login')


user=get_user_model
def login_view(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        global user_login
        # global user
        try:
            user_login = Login.objects.get(email=email)
            print(user_login)
            if user_login is not None and user_login.password==password:  
                CustomUser = get_user_model()
                user = authenticate(request,email=email,password=password)
                print("user is:--- ",user.name)
                if user is not None :
                    login(request,user)
                    return redirect('dashboard')
                    # return render(request,'login/dashboard.html')
                else:
                    context = {'error_message': 'Invalid email or password'}
                    return render(request, 'login/login.html', context)
            else:
                context = {'error_message': 'Invalid email or password'}
                return render(request, 'login/login.html', context)
        except Login.DoesNotExist:
            user_login = None
            print(user_login)
            context = {'error_message': 'You are User Not Admin'}
            return render(request, 'login/login.html', context)
    else:
            return render(request, 'login/login.html')


def logout_Admin(request):
    logout(request)
    return redirect('login')

def dashboard(request):
    print(request)
    print(request.user)
    print(request.user.is_authenticated)
    if request.user.is_authenticated:
        user = request.user
        fname = user.name
        return render(request,'login/dashboard.html',{'name':fname})
    else:
        # context = {'error_message': 'Invalid email or password'}
        # return render(request, 'login/login.html', context)
        return redirect('login')

def list_of_paper(request, conference__id):
    if request.user.is_authenticated:
        user = request.user
        context={
            'paper':paper.objects.filter(conference_id=conference__id),
            'user':request.user
        }
        return render(request,'login/papers_list.html',context)
    else:
        return redirect('login')

def list_of_conference(request):
    if request.user.is_authenticated:
        user = request.user
        print("He Check The Conference List",user.name)
        context={
            'conference':conference.objects.all()
        }
        return render(request,"login/conferences_list.html",context)
    else:
        return redirect('login')

def update_paper_status(request, selected_paper_id):
    if request.user.is_authenticated and request.method == 'POST':
        new_status = request.POST.get('status')
        papers = get_object_or_404(paper, id=selected_paper_id)
        papers.status = new_status
        papers.save()
        return redirect('list-of-conference')
    else:
        return redirect('login')

def create_conference(request):
    if request.user.is_authenticated:
        user = request.user
        fname = user.name
        conferences = conference.objects.all()
        if request.method == 'POST':
            conference_name = request.POST.get('conference_name')
            conference_description = request.POST.get('conference_description')
            conference_end_date = request.POST.get('conference_end_date')
            New_Conference = conference.objects.create(
                conference_name=conference_name,conference_descriptions=conference_description,
                conference_end_date=conference_end_date
            )
            New_Conference.save()
            context_success = {'success_message': 'Your Conference Created Successfully :-) '}
            return render(request, 'login/create_conference.html', context_success)
        else:
            return render(request,'login/create_conference.html',{'name':fname})
    else:
        # context = {'error_message': 'Invalid email or password'}
        # return render(request, 'login/login.html', context)
        return redirect('login')