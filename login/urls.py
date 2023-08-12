"""Login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from login import views

urlpatterns = [
    path('',views.login_view,name="login"),
    path('login/',views.login_view,name="login"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path('dashboard/list-of-paper/<int:conference__id>/',views.list_of_paper,name="list-of-paper"),
    path('dashboard/list-of-paper/update-paper-status/<int:selected_paper_id>/', views.update_paper_status, name='update_paper_status'),
    path('dashboard/create-conference/',views.create_conference,name="create_conference"),
    path('dashboard/list-of-conference/',views.list_of_conference,name="list-of-conference"),
    path('logout/',views.logout_Admin,name="logout_Admin"),
   
]
