from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseGone

# Create your views here.

def home(response):
    return render(response, 'chat/home.html', {})

def chat(response):
    return render(response, 'chat/chat.html', {})

def characters(response):
    return render(response, 'chat/char.html', {})