from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import ItemDataTableSerializer

from django.shortcuts import redirect, render

from .models import Item, City
from .forms import ItemForm


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

# Item Model Functions

def ItemList(request):
     form = ItemForm()  
     return render(request, 'adminPanel/item_list.html', {'form': form})

def AddItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:item_list')  # Redirect to a list view or any other view
    else:
        form = ItemForm()
    return render(request, 'adminPanel/add_item.html', {'form': form})