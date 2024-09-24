from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *

def home(request):
    return render(request, "authentication/main.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not Customer_user.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect("login")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("login")
        else:
            login(request, user)
            return redirect("index")
        
    return render(request, "authentication/login.html")

def log_out(request):
    logout(request)
    return redirect("login")

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = Customer_user.objects.filter(username = username)

        if user.exists():
            messages.error(request, "Username already taken!")
            return redirect("register")
        
        user = Customer_user.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username  = username
        )

        user.set_password(password)
        user.save()
        messages.info(request, "Account created Successfully!")
        return redirect("login")
    
    return render(request, "authentication/register.html")
    