from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path("",views.home,name="home"),
    path("send_otp",views.send_otp,name="send otp"),
    path("save",views.save,name="save"),
    path("signin",views.signin,name="signin"),
    path("user_page",views.user_page,name="user_page"),
   
   
]
