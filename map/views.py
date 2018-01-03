from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Position

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'map/map_container.html')

@csrf_exempt
def set_bounds_map(request):
    print("lat NE = "+request.POST['latne']+"lng NE = "+request.POST['lngne']+"lat SW = "+request.POST['latsw']+"lng SW = "+request.POST['lngsw'])
    return HttpResponse("gyigiy")
