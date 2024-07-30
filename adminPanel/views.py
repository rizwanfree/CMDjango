from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import ItemDataTableSerializer

from django.shortcuts import render

from .models import Item, City


# API CALLS

class ItemDataTableAPI(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemDataTableSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
# Create your views here.

def Dashboard(request):
    return render(request, 'adminPanel/dashboard.html')


def CityList(request):
     cities = City.objects.all()

     context = {
          'cities': cities,
     }
     return render(request, 'adminPanel/citylist.html', context)

def ItemList(request):
     
     return render(request, 'adminPanel/item_list.html')