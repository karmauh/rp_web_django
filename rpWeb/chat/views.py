from pyexpat import model
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseGone
from .models import *
from django.views.generic import CreateView, DetailView

# Create your views here.

def home(response):
    return render(response, 'chat/home.html', {})

def chat(response):
    return render(response, 'chat/chat.html', {})

def characters(response):
    data = Character.objects.all()
    return render(response, 'chat/char.html', {'data': data})
    
class createCharacter(CreateView):
    model = Character
    template_name = 'chat/create.html'
    fields = '__all__'