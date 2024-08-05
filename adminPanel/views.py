from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.decorators.http import require_POST

from .models import Item, City, Port, ShippingLine
from .forms import ItemForm, PortForm, ShippingLineForm


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

# Port
class PortListView(ListView):
    model = Port
    template_name = 'adminPanel/Port/Port-List.html'
    context_object_name = 'ports'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PortForm()  # Empty form for creating new port
        return context


class PortDetailView(DetailView):
    model = Port
    template_name = 'adminPanel/Port/port-details.html'
    context_object_name = 'port'


class PortCreateView(CreateView):
    model = Port
    form_class = PortForm
    template_name = 'adminPanel/Port/Port-Form.html'
    success_url = reverse_lazy('adminPanel:port-list')


class PortUpdateView(UpdateView):
    model = Port
    form_class = PortForm
    template_name = 'adminPanel/Port/port-form.html'
    success_url = reverse_lazy('adminPanel:port-list')

@require_POST
def PortDelete(request, pk):
    port = get_object_or_404(Port, pk=pk)
    port.delete()
    messages.success(request, 'Port deleted successfully.')
    return redirect('adminPanel:port-list')  # Redirect to the port list

# End Port

# Shipping Line
class ShippingListView(ListView):
    model = ShippingLine
    template_name = 'adminPanel/ShippingLine/shippingline-List.html'
    context_object_name = 'shippings'

class ShippingDetailView(DetailView):
    model = ShippingLine
    template_name = 'adminPanel/Port/port-details.html'
    context_object_name = 'shipping'


class ShippingCreateView(CreateView):
    model = ShippingLine
    form_class = ShippingLineForm
    template_name = 'adminPanel/ShippingLine/shippingline-form.html'
    success_url = reverse_lazy('adminPanel:port-list')


class ShippingUpdateView(UpdateView):
    model = ShippingLine
    form_class = ShippingLineForm
    template_name = 'adminPanel/ShippingLine/shippingline-form.html'
    success_url = reverse_lazy('adminPanel:shipping-list')

@require_POST
def ShippingDelete(request, pk):
    shipping = get_object_or_404(ShippingLine, pk=pk)
    shipping.delete()
    messages.success(request, 'Shipping Line deleted successfully.')
    return redirect('adminPanel:shipping-list')  # Redirect to the port list

# End Port