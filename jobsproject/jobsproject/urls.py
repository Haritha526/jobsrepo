"""
URL configuration for jobsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from jobsapp import views
urlpatterns = [
    path('', views.homepage_view),
    path('hydjobs/', views.hydjobs_view),
    path('punejobs/', views.punejobs_view),
    path('bngjobs/', views.bngjobs_view)
]
