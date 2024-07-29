from django.shortcuts import render

from .models import City

# Create your views here.

def Dashboard(request):
    return render(request, 'adminPanel/dashboard.html')


def CityList(request):
     cities = City.objects.all()

     context = {
          'cities': cities,
     }
     return render(request, 'adminPanel/citylist.html', context)