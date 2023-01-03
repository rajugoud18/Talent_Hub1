"""Talent_Hub URL Configuration

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
from django.urls import path
from careerapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home , name='home'),
    path('info/',views.info ,name='info'),
    path('inter/',views.Inter, name='inter'),
    path('diploma/',views.Diploma , name='Diploma'),
    path('iiit/',views.IIIT, name='IIIT'),
    path('iti/',views.ITI,name='ITI'),
    path('Vocational/',views.Vocational,name="Vocational"),
    path('Travel/',views.Travel,name='Travel'),
    path('sports/',views.Sports,name='sports'),
    path('jobs/',views.Govt_jobs,name='Govt_jobs'),
    path('skills/',views.SKills,name='Skills'),
    path('details/',views.details,name='details'),
    path('bank_details/',views.bank_details,name='bank_details'),
    path('donations/',views.donations,name='donations'),
]
