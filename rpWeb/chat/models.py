from django.db import models

# Create your models here.

class char(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    age = models.DecimalField(max_digits=12, decimal_places=0, blank=True)
    race = models.CharField(max_length=100)
    appearance = models.TextField(max_length=500)
    short_hisotry = models.TextField(max_length=500)
    
    
    def __str__(self):
        return self.first_name