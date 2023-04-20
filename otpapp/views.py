from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random
from.models import user
def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    phone=request.GET.get("phone")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'<phone id>',[phone],fail_silently=False,html_message=htmlgen)
    return HttpResponse(o)

def home(request):
    return render(request, "home.html")


def save (request):
    n=request.POST['name']
    p=request.POST['phone1']
    data=user(name=n,phone=p)
    data.save()
    return render(request,'home.html',{'msg':"user can signup"})

def signin(request):
    return render(request, "sign_in.html")

def user_page(request):
    data=user.objects.all()
    return render(request,'user_page.html',{'phone':data})



       
      

