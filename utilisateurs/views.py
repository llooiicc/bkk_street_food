from django.shortcuts import render
from django.contrib.auth import authenticate, login as log, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

# Create your views here.

@require_http_methods(["POST" , "GET"])
def login(request):
    
    if request.method == "GET" :
        print(request.method)
        return render(request, 'utilisateurs/login.html')
    else :
        login = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=login, password=password)

        if user is not None :
            log(request, user)
            print(request.user.is_authenticated())
            return render(request, 'utilisateurs/login.html', {
                "error": "success !"

            })
        else :
            return render(request, 'utilisateurs/login.html' , {
                "error": "invalid login or password"
            })


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
    