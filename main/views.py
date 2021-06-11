from django.shortcuts import render,redirect
from django.http import HttpResponse
from passlib.hash import pbkdf2_sha256,bcrypt
from main.models import StationDetails,TrainDetails,User,Ticket
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

def userRegister(request):
    u = User()
    userid = request.POST['user_id']
    u.user_id = userid
    u.password = encryptPassword(request.POST['password'])
    u.name = request.POST['user_name']
    u.email = request.POST['user_email']
    print("text received successfully.....testing profile pic")
    i = request.FILES['pro_pic'].name.split(".")
    print("intially : ",request.FILES['pro_pic'].name)
    request.FILES['pro_pic'].name = userid + "." + i[-1]
    u.profile_pic = request.FILES['pro_pic']
    print("pic stored succesfully")
    u.save()
    return render(request,'loginform.html')

def loginstation(request):
    return render(request,'loginstation.html')

def login(request):
    return render(request,'login.html')



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

def trainList():
    return TrainDetails.objects.all()

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

def Log(request):
    print(request.POST['id'])
    u = User.objects.get(user_id=request.POST['id'])
    password = request.POST['pass']
    if pbkdf2_sha256.verify(password,u.password):
        response = render(request,'Userlogin.html',{'t':trainList(),'u':u}) 
        #t=list of trains , u = user object
        response.set_cookie(key="user_id", value=u.user_id)
        # cookie set
    return response    
    #return HttpResponse("wrong password")

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
    


def Userlogin(request):
    return render(request,'Userlogin.html')




def passenger_details(request):
    max = request.POST['max']
    print(max)
    # get a date field from front end
    saveTicket(request.COOKIES.get('user_id'),request.POST['train'],request.POST['name'],request.POST['age'],request.POST['uid'],request.FILES['faceImage'])
    t1 = Ticket(user_id=request.COOKIES.get('user_id'))
    print("ticket booked for 1st passenger")
    if(max == '2'): 
        print('max is 2')
        saveTicket(request.COOKIES.get('user_id'),request.POST['train'],request.POST['name1'],request.POST['age1'],request.POST['uid1'],request.FILES['faceImage1'])
        print("ticket booked for 2nd passenger ")
        # t2 = Ticket(user_id=request.COOKIES.get('user_id'),train_no=request.POST['train'])
        # t2.passenger_name = request.POST['name1']
        # t2.age = request.POST['age1']
        # t2.uid = request.POST['uid1']
        # t2.image = rename(request.FILES['faceImage1'],t2.uid)
        # t2.save()
    elif(max == '3'):
        # t3 = Ticket(user_id=request.COOKIES.get('user_id'),train_no=request.POST['train'])
        saveTicket(request.COOKIES.get('user_id'),request.POST['train'],request.POST['name1'],request.POST['age1'],request.POST['uid1'],request.FILES['faceImage1'])
        print("ticket booked for 2nd passenger ")
        saveTicket(request.COOKIES.get('user_id'),request.POST['train'],request.POST['name2'],request.POST['age2'],request.POST['uid2'],request.FILES['faceImage2'])
        print("ticket booked for 3rd passenger")
        # name = request.POST['name1']
        # name2 = request.POST['name2']
        # age1 = request.POST['age1']
        # age2 = request.POST['age2']
        # uid1 = request.POST['uid1']
        # uid2 = request.POST['uid2']
        # image1 = request.FILES['faceImage1']
        # image2 = request.FILES['faceImage2']
        # print(train, max, name, name1, name2, age, age1, age2, uid, uid1, uid2, image, image1, image2)
    return render(request,'Userlogin.html')

def rename(pic,uid):
    print("intially : ",pic.name)
    i = pic.name.split(".")
    pic.name = uid + "." + i[-1]
    print("later : ",pic.name)
    return pic

def saveTicket(user_id,train_no,name,age,uid,image):
    t = Ticket(user_id=user_id,train_no=train_no,passenger_name=name,age=age,uid=uid)
    t.image = rename(image,uid)
    t.save()