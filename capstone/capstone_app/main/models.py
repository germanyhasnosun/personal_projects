from django.db import models

# Create your models here.

class meta_data(models.Model):
    outcome = models.CharField(max_length=50)
    outcome_integer = models.IntegerField(default = None, blank = True, null=True)
    age =  models.CharField(max_length=50)
    age_integer = models.IntegerField(default = None, blank = True,  null=True)
    sex =  models.CharField(max_length=50)
    sex_integer = models.IntegerField(default = None, blank = True, null=True)
    location = models.CharField(max_length=50)
    location_integer = models.IntegerField(default = None, blank = True, null=True)

class Image(models.Model):
    image = models.ImageField(upload_to='')
