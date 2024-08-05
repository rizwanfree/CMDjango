from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from .models import Item, City
from .forms import ItemForm


def Dashboard(request):
    return render(request, 'adminPanel/dashboard.html')


def CityList(request):
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'adminPanel/citylist.html', context)


def ItemList(request):
    if request.method == 'POST':
        item_id = request.POST.Get('item_id')
        if item_id:  # Update existing item
            item = get_object_or_404(Item, pk=item_id)
            form = ItemForm(request.POST, instance=item)
        else:  # Add new item
            form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('adminPanel:item_list')

    items = Item.objects.all()
    form = ItemForm()
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


def ClientEdit(request, id=None):
    if id:
        # Editing an existing client
        item = get_object_or_404(Item, id=id)
        form = ItemForm(request.POST or None, instance=item)
    else:
        # Creating a new client
        form = ItemForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Item saved successfully.')
            return redirect('adminPanel:item_list')  # Redirect to a list view or any other view as needed

    context = {
        'form': form,
        'id': id,
    }
    return render(request, 'adminPanel/add_item.html', context)
