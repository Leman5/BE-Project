from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('templates/loginform.html',views.loginform),
    path('templates/log',views.Log),
    path('templates/loginstation.html',views.loginstation),
    path('templates/login.html',views.login),
    path('templates/adminlogcredentials',views.adminlogcredentials),
    path('templates/Station-list.html',views.Stationlist),
    path('templates/logout.html',views.adminlogout),
    path('templates/Add-trains.html',views.Addtrains),
    path('templates/Add-station.html',views.Addstation),
    path('/templates/addstation',views.AddStationDetails)
    
    
]