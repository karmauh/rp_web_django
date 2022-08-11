from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Chararacter(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    age = models.DecimalField(max_digits=12, decimal_places=0, blank=True)
    race = models.CharField(max_length=100)
    appearance = models.TextField(max_length=500)
    short_hisotry = models.TextField(max_length=500)
        
    def __str__(self):
        return self.first_name + ' | ' + str(self.author)
    
    
# class Author(models.Model):
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     def __str__(self):
#         return User.objects.get(Author=self.author)
    
#     class Meta:
#         ordering = ['author']