from django.db import models

# Create your models here.
class StationDetails(models.Model):
    station_username = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=255,default=None)
    email = models.EmailField(max_length=200,unique=True)
    fname = models.CharField(max_length=255,default=None,null=True)
    lname = models.CharField(max_length=255,null=True)
    city = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=50,null=True)
    pincode = models.CharField(max_length=10,null=True)