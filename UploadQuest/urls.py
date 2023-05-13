from django.contrib import admin
from django.urls import path
from UploadQuest import views
urlpatterns = [
    path('',views.index,name="Upload"),
    path('upload',views.index,name="Upload"), 
    path('login',views.loginuser,name="loginuser"),
    path('logout',views.logoutuser,name="index"),
    path('account',views.account,name="Account Information"),
]
