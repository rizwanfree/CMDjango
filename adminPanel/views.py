from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Item, City, Port
from .forms import ItemForm, PortForm


def Dashboard(request):
    return render(request, 'adminPanel/dashboard.html')


def CityList(request):
    cities = City.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'adminPanel/City/citylist.html', context)


def ItemList(request):
    return render(request, 'adminPanel/Item/item_list.html')


def ItemEdit(request, id=None):
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
    return render(request, 'adminPanel/Item/add_item.html', context)


class PortListView(ListView):
    model = Port
    template_name = 'adminPanel/Port/Port-List.html'
    context_object_name = 'ports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PortForm()  # Empty form for creating new port
        return context


class PortCreateView(CreateView):
    model = Port
    form_class = PortForm
    template_name = 'adminPanel/Port/Port-Form.html'
    success_url = reverse_lazy('adminPanel:port-list')


class PortUpdateView(UpdateView):
    model = Port
    form_class = PortForm
    template_name = 'adminPanel/Port/Port-Form.html'
    success_url = reverse_lazy('adminPanel:port-list')
