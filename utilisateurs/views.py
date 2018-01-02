from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["POST" , "GET"])
def login(request):
    
    if request.method == "GET" :
        return render(request, 'vues/constacts.html')
    else :
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
    