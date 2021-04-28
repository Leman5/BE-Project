from django.shortcuts import render,redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256,bcrypt
from main.models import StationDetails
import cv2

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
    return render(request,'Add-station.html')

def stationlogcredentials(request):
    return render(request,'Verify-passenger.html')

def verifypassengers(request):
    return render(request,'Verify-passenger.html')

def updateprofile(request):
    return render(request,'Update-profile.html')

def slogout(request):
    return render(request,'S-logout.html')

def verify(request):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    while True:
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y),(x+w, y+h),(255, 0, 0), 2) 
        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff
        if k==27:
            break
    cap.release()

    return render(request,'Verify-passenger.html')
    
