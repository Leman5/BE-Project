from django.shortcuts import render,redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256,bcrypt
from main.models import StationDetails

# Create your views here.

def home(request):
    print("Inside Home")
    return render(request,'index.html')

def loginform(request):
    print("user login")
    return render(request,'loginform.html')

def loginstation(request):
    return render(request,'loginstation.html')

def login(request):
    return render(request,'login.html')

def Log(request):
    print(request.POST['id'])
    print(request.POST['pass'])
    return render(request,'loginform.html')


def adminlogcredentials(request):
    if request.POST['id'] == 'admin' and request.POST['pass'] == 'admin123' :
        return render(request,'Add-station.html')

def Stationlist(request):
        return render(request,'Station-list.html')

def adminlogout(request):
        return render(request,'logout.html')

def Addtrains(request):
        return render(request,'Add-trains.html')

def Addstation(request):
        return render(request,'Add-station.html')

def AddStationDetails(request):
    s = StationDetails()
    s.station_username = request.POST['username']
    s.password = request.POST['password']
    s.email = request.POST['email']
    s.fname = request.POST['fname']
    s.lname = request.POST['lname']
    s.city = request.POST['city']
    s.state = request.POST['state']
    s.pincode = request.POST['pincode']
    s.save()
    return HttpResponse('')