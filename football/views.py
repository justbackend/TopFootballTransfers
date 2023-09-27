from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    return render(request, "index.html")

def clubs(request):
    content = {
        "clubs": Club.objects.all()
    }
    return render(request, "clubs.html", content)