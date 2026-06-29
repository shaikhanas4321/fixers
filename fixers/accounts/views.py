from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
# Create your views here.
def index(request):
    return render(request,"accounts/index.html")


def login_view(request):
    if request.method == "POST":
        username1=request.POST.get("username")
        password1=request.POST.get("password")
        user=authenticate(request , username=username1 ,password=password1)
        if user is not None:
            login(request , user)
            return HttpResponseRedirect(reverse("services:index"))
        else:   
         return render(request ,"accounts/login.html",{
           "message":"not authenticated"
     })
    else:
       return render(request ,"accounts/login.html")





def register(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
        user_type=request.POST.get("user_type")
        print(request.POST)
        print(request.POST.get("user_type"))
        if password != confirmation:
            return render(request, "accounts/register.html", {
                "message": "Passwords must match"
            })
        try:
            user = User.objects.create_user(username=username,email=email,password=password,user_type=user_type)
            print("user created")
            print(user)
            if user_type == "CUSTOMER": 
                CustomerProfile.objects.create(user=user)

            elif user_type == "PROVIDER":
                ProviderProfile.objects.create(user=user)

        except IntegrityError as e:
             print("ERROR:", type(e))
             print("ERROR MESSAGE:", e)
             return render(request, "accounts/register.html", {
                "message": "Username already exists"
            })

        login(request, user)
        return HttpResponseRedirect(reverse("services:index"))

    return render(request, "accounts/register.html")

