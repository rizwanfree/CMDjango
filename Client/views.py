from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.http import require_POST
from .forms import ClientForm

from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages

from .models import Client


# Create your views here.

def ClientList(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'Client/client_list.html', context)


def ClientDetails(request, id):
    client = get_object_or_404(Client, id=id)

    context = {
        'client': client
    }
    return render(request, 'Client/client_details.html', context)


def ClientEdit(request, id=None):
    if id:
        # Editing an existing client
        client = get_object_or_404(Client, id=id)
        form = ClientForm(request.POST or None, instance=client)
        print(id)
    else:
        # Creating a new client
        form = ClientForm(request.POST or None)
        print(id)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Client saved successfully.')
            return redirect('client:client-list')  # Redirect to a list view or any other view as needed

    context = {
        'form': form,
        'id': id,
    }
    print(id)
    return render(request, 'client/client_edit.html', context)


@require_POST
def DeleteClient(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    messages.success(request, 'Client deleted successfully.')
    return redirect('client:client-list')  # Redirect to the client list or another appropriate page
