from pyexpat import model
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseGone
from .models import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.

def home(response):
    return render(response, 'chat/home.html', {})

def chat(response):
    return render(response, 'chat/chat.html', {})

def characters(request):
    data = Character.objects.all()
    file = Character(request.FILES)
    return render(request, 'chat/char.html', {'data': data, 'file': file})

 
class createCharacter(SuccessMessageMixin ,CreateView):
    model = Character
    template_name = 'chat/create.html'
    fields = '__all__'
    success_url = reverse_lazy('create_home')
    success_message = 'New Character created successfully'

def create_home(request):
    return render(request, 'chat/char.html')