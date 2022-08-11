from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='character', null=True)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    age = models.DecimalField(max_digits=12, decimal_places=0, blank=True)
    race = models.CharField(max_length=100)
    appearance = models.TextField(max_length=500)
    short_hisotry = models.TextField(max_length=500)
    complete = models.BooleanField(default=True)
        
    def __str__(self):
        return self.first_name + ' | ' + str(self.user) + ' | ' + str(self.complete)