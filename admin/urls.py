from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.adminloginpage),
    path('authenticate/',views.adminauthenticate),
    path('dashboard/', views.admindashboard),
    path('logout/', views.adminlogout),
    path('smartcontract/',views.smartcontractview),
    path('signerstatus/', views.checksignerview),
    path('signer/',views.checksigner),
    path('searchvoterdb/',views.checkvoterdbview),
    path('searchdb/',views.voterdata),

]