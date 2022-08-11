from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character', null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    age = models.DecimalField(max_digits=12, decimal_places=0, null=True)
    race = models.CharField(max_length=100, null=True)
    appearance = models.TextField(max_length=500, null=True)
    short_hisotry = models.TextField(max_length=500, null=True)
        
    def __str__(self):
        return self.first_name + ' | ' + str(self.user)
    
    def get_absolute_url(self):
        return reverse('app_name : create') #do naprwy