from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseGone
from .models import *

# Create your views here.

def home(response):
    return render(response, 'chat/home.html', {})

def chat(response):
    return render(response, 'chat/chat.html', {})

def characters(response):
    data = Character.objects.all()
    return render(response, 'chat/char.html', {'data': data})

def create(response):
    return render(response, 'chat/create.html')