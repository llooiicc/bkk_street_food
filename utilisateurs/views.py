from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def login(request):
    
    login = request.POST['login']
    password = request.POST['password']
    
    user = authenticate(request, username=login, password=password)
    
    if user is not None :
        login(request, user)
        
    else :
        pass
    

def logout(request):
    logout(request)


def signup(request):
    
    login = request.POST['login']
    password = request.POST['password']
    
    u = User()
    u.username = login
    u.password = password
    u.email = login
    
    u.save()
    