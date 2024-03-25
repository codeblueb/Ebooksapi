from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth

# from django.views.generic import UserCreationForm
from django.urls import reverse_lazy 
from .forms import RegisterForm

from .models import CustomUser

def home(request):
    
    return render(request, 'home.html')

def login(request):
    
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            messages.success(request, 'You are logged in')
            auth.login(request, user)
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return redirect('login')        
    return render(request, 'login.html')


# class RegisterForm(UserCreationForm):
#     form_class = 

def register(request):
        
    if request.method == "POST":
        
        form = RegisterForm(request.POST or None)
        
        if form.is_valid():
                
            if CustomUser.objects.filter(username=form.cleaned_data["username"]).exists():
                messages.warning(request, 'This username exists')
                return redirect('register')
            if CustomUser.objects.filter(email=cleaform.cleaned_dataned_data["email"]).exists():
                messages.warning(request, 'This email exists')
                return redirect('register')
                
            if CustomUser.objects.filter(username=form.cleaned_data["username"]).exists() and CustomUser.objects.filter(email=form.cleaned_data["email"]).exists():
                messages.warning(request, "Username and Email eixsts")
                return redirect('register')
            else:
                # user = CustomUser.objects.create_user(username=cleaned_data["username"], 
                #                                       email=cleaned_data["email"], 
                #                                       password=cleaned_data["password"])
                user = form.save()
                user.save()
                auth.login(request, user)
                messages.success(request, 'Registered, and logged in successfully')
                return redirect('home')
    else:
        form = RegisterForm() # empty form 

    return render(request, 'register.html', {"form":form})


def logout(request):
    
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, "You have been logged out")
        return redirect('home')
    return render(request, 'logout.html')

def user_list(request):
    
    profiles = CustomUser.objects.all()
    return render(request, 'users_list.html', {'profiles':profiles})

def user_details(request, pk):
    
    return render(request, 'user_details.html')
