from django.shortcuts import render,redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256,bcrypt
from main.models import StationDetails,TrainDetails
import cv2

# Create your views here.
def encryptPassword(password):
    encrypted = pbkdf2_sha256.encrypt(password,rounds = 1200,salt_size=40)
    print("password encrypted")
    return encrypted

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
    s = StationDetails.objects.all()
    return render(request,'Station-list.html',{'s':s}) #object s has all the stations...use it to display in the table

def adminlogout(request):
        return render(request,'logout.html')

def Addtrains(request):
    return render(request,'Add-trains.html')

def AddtrainsDetails(request):
    t = TrainDetails()
    t.fromstation = request.POST['fromstation']
    t.tostation = request.POST['tostation']
    t.trainno = request.POST['trainno']
    t.save()
    return render(request,'Add-trains.html')

def Addstation(request):
        return render(request,'Add-station.html')

def AddStationDetails(request):
    s = StationDetails()
    s.station_username = request.POST['username']
    s.password = encryptPassword(request.POST['password'])
    s.email = request.POST['email']
    s.fname = request.POST['fname']
    s.lname = request.POST['lname']
    s.city = request.POST['city']
    s.state = request.POST['state']
    s.pincode = request.POST['pincode']
    s.save()
    return render(request,'Add-station.html')

def stationlogcredentials(request):
    print(request.POST['uname'])
    s = StationDetails.objects.get(station_username=request.POST['uname'])
    password = request.POST['pass']
    if pbkdf2_sha256.verify(password,s.password):
        response = render(request,'Verify-passenger.html')
    return response

def verifypassengers(request):
    return render(request,'Verify-passenger.html')

def updateprofile(request):
    return render(request,'Update-profile.html')

def updatestation(request):
    s = StationDetails.objects.get(station_username=request.POST['username'])
    s.password = encryptPassword(request.POST['password'])
    s.email = request.POST['email']
    s.fname = request.POST['fname']
    s.lname = request.POST['lname']
    s.save()
    print("station updated")
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
    
