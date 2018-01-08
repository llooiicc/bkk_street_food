from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from articles.models import Article
from django.db.models import Q

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

    articles = Article.objects.filter(Q(lat__gte=lat_sw) & Q(lat__lte=lat_ne)).filter(Q(lng__gte=lng_sw) & Q(lng__lte=lng_ne))
    for a in articles:
        positions[a.id] = {"lat": a.lat ,"lng": a.lng, "titre": a.titre}
    return JsonResponse(positions)
