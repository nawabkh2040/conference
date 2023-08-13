"""Singup URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from singup import views

urlpatterns = [
    path('',views.singup_view,name="singup"),
    path('singin/',views.singIn,name="singin"),
    path('success/', views.success_view, name='success'),
    path('success/logout/',views.logout_page,name="logout"),
    path('activate/<str:uidb64>/<str:token>/',views.activate,name="activate"),
    path('success/conference_detail/<int:conf_id>/submit/',views.submit_paper,name="submit"),
    path('success/conference_detail/resubmit/<int:paper_id>',views.resubmit,name="resubmit"),
    path('success/list-of-Papers/<int:conf_id>',views.list_of_paper,name="list_of_paper"),
    path('success/list-of-conference/',views.list_of_conference,name="list_of_conference"), 
    path('success/conference_detail/<int:conf_id>/', views.conference_detail, name='conference_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)