"""
URL configuration for f_transfer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from football.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path("clubs/", clubs),
    path('u-20', u_20),
    path('england', england),
    path('country-clubs', country_clubs),
    path('players', players),
    path('transfer-records', transfer_records),
    path('transfer-archive', transfer_archive),
]
