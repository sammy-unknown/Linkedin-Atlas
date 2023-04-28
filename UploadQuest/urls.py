from django.contrib import admin
from django.urls import path
from UploadQuest import views
urlpatterns = [
    path('',views.index,name="Upload"),
    path('upload',views.index) 
]
