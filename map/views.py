from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from articles.models import Position

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, 'map/map_container.html')

@csrf_exempt
def set_bounds_map(request):
    print("lat NE = "+request.POST['latne']+"lng NE = "+request.POST['lngne']+"lat SW = "+request.POST['latsw']+"lng SW = "+request.POST['lngsw'])
    lat_ne = float(request.POST['latne'])
    lng_ne = float(request.POST['lngne'])
    lat_sw = float(request.POST['latsw'])
    lng_sw = float(request.POST['lngsw'])
    positions = {}

    for p in Position.objects.all():
        if p.lat >= lat_sw and p.lat <= lat_ne:
            print('lat ok')
            if p.lng >= lng_sw and p.lng <= lng_ne:
                print('lng ok')
                print(p.id)
                positions[p.article_id] = [p.lat, p.lng]

    return JsonResponse(positions)
