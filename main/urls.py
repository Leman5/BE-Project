from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('templates/loginform.html',views.loginform),
    path('templates/log',views.Log),
    path('templates/loginstation.html',views.loginstation),
    path('templates/login.html',views.login)
]