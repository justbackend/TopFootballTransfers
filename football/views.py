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

def u_20(request):
    return render(request, 'U-20 players.html')

def england(request):
    return render(request, 'england.html')

def country_clubs(request):
    return render(request, 'country-clubs.html')

def players(request):
    content = {
        'players': Player.objects.all()
    }

    return render(request, 'players.html', content)

def transfer_records(request):
    content = {
        "transfers": Transfer.objects.all()
    }
    return render(request, 'transfer-records.html', content)

def transfer_archive(request):
    return render(request, 'transfer-archive.html')