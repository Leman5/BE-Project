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