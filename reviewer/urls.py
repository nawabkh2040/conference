"""conference URL Configuration

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
from reviewer import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    
    path('',views.index,name='index'),
    path('sing-up/',views.sing_up_reviewer,name='reviewer-sing-up'),
    path('sing-in/',views.sing_in_reviewer,name='reviewer-sing-in'),
    path('sing-out/',views.sing_out_reviewer,name='reviewer-sing-out'),
    path('dashboard/',views.dashboard_reviewer,name='reviewer-dashboard'),
    path('activate-reviewer/<str:uidb64>/<str:token>/',views.activate_reviewer,name="activate_reviewer"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
