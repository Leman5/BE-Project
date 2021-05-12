from . import views
from django.urls import path

urlpatterns = [

    path('',views.home,name='home'),
    path('templates/loginform.html',views.loginform),
    path('templates/log',views.Log),
    path('templates/loginstation.html',views.loginstation),
    path('templates/new_user_register',views.userRegister),
    path('templates/login.html',views.login),
    path('templates/adminlogcredentials',views.adminlogcredentials),
    path('templates/Station-list.html',views.Stationlist),
    path('templates/logout.html',views.adminlogout),
    path('templates/Add-trains.html',views.Addtrains),
    path('templates/Add-station.html',views.Addstation),
    path('templates/addstation',views.AddStationDetails),
    path('templates/stationlogcredentials',views.stationlogcredentials),
    path('templates/Verify-passenger.html',views.verifypassengers),
    path('templates/Update-profile.html',views.updateprofile),
    path('templates/S-logout.html',views.slogout),
    path('templates/verify',views.verify),
    path('templates/Update-station',views.updatestation), 
    path('templates/AddtrainsDetails',views.AddtrainsDetails)

    
    
]