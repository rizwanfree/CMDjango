from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .Serializer import ClientDataTableSerializer

from django.shortcuts import render

from .models import Client


# API CALLS

class ClientDataTableAPI(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientDataTableSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create your views here.

def ClientList(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'Client/client_list.html', context)