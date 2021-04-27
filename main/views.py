from django.shortcuts import render
from django.http import HttpResponse

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
        return render(request,'Add station.html')

def Stationlist(request):
        return render(request,'Station list.html')

def adminlogout(request):
        return render(request,'logout.html')

def Addtrains(request):
        return render(request,'Add trains.html')

def Addstation(request):
        return render(request,'Add station.html')