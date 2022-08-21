from email.policy import default
from tkinter.messagebox import showinfo
from xml.dom.minidom import Attr
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Character(models.Model):
    author = models.ForeignKey(User, db_index=True, null=True, default=User, on_delete=models.CASCADE)
    #author = models.CharField(max_length=50, default=User, editable=False)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    age = models.DecimalField(max_digits=12, decimal_places=0, null=True)
    race = models.CharField(max_length=100, null=True)
    appearance = models.TextField(max_length=500, null=True)
    short_hisotry = models.TextField(max_length=500, null=True)
    img = models.ImageField(null=True, blank=True, upload_to='images/')
        
    def __str__(self):
        return self.first_name + ' | ' + str(self.author)