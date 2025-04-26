from django.db import models

# Create your models here.

class profile(models.Model):
    # all the things that will be asked in the form
    # does not include final label 
    
    age = models.IntegerField()
    haemoglobin = models.FloatField()
    wbc = models.FloatField()
    differential = models.FloatField()
    rbc = models.FloatField()
    platelet = models.FloatField()
    pdw = models.FloatField()
