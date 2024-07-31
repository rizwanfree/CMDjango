from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import ItemDataTableSerializer

from django.shortcuts import redirect, render, get_object_or_404

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
    if request.method == 'POST':
        # Determine if we are editing an existing item or adding a new one
        item_id = request.POST.get('item_id')
        if item_id:  # If item_id is present, we're editing
            item = get_object_or_404(Item, pk=item_id)
            form = ItemForm(request.POST, instance=item)
        else:  # Else, we're adding a new item
            form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('adminPanel:item_list')
    else:
        form = ItemForm()

    items = Item.objects.all()
    return render(request, 'adminPanel/item_list.html', {'items': items, 'form': form})

def AddItem(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:item_list')  # Redirect to a list view or any other view
    else:
        form = ItemForm()
    return render(request, 'adminPanel/add_item.html', {'form': form})

def EditItem(request, id=None):
    if id:
        # Editing an existing client
        item = get_object_or_404(Item, id=id)
        form = ItemForm(request.POST or None, instance=item)
    else:
        # Creating a new client
        form = ItemForm(request.POST or None)

    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminPanel:item_list')  # Redirect to a list view or any other view
    else:
        form = ItemForm()
    return render(request, 'adminPanel/add_item.html', {'form': form})