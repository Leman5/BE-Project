from django.db import models
from main.storage import OverwriteStorage

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

class TrainDetails(models.Model):
    trainno = models.CharField(max_length=10,unique=True)
    fromstation = models.CharField(max_length=255,null=True)
    tostation = models.CharField(max_length=255,null=True)

def user_directory_path(instance, filename):
    return filename

class User(models.Model):
    user_id = models.CharField(max_length=100,primary_key=True)
    password = models.CharField(max_length=255,default=None)
    name = models.CharField(max_length=255,default=None,null=True)
    email = models.EmailField(max_length=200,unique=True)
    profile_pic = models.FileField(upload_to=user_directory_path,blank=True, null=True)

def uid_directory_path(instance, filename):
    return '{0}/{1}'.format("uid_pics", filename)

class Ticket(models.Model):
    user_id = models.CharField(max_length=100,null=True)
    train_no = models.CharField(max_length=10)
    date = models.CharField(max_length=100,null=True,default=None)
    passenger_name = models.CharField(max_length=100,null=True)
    uid = models.CharField(max_length=100,null=True,unique=True)
    age = models.IntegerField()
    image = models.FileField(upload_to=uid_directory_path,storage=OverwriteStorage(),blank=True, null=True)
    boarded = models.CharField(max_length=10,default="False")