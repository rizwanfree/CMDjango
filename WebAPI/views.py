from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from WebAPI.Serializers.ClientSerializer import ClientDataTableSerializer
from Client.models import Client
from WebAPI.Serializers.ItemSerializer import ItemDataTableSerializer
from adminPanel.models import Item


# Create your views here.

# Client APIs
class ClientDataTableAPI(APIView):
    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientDataTableSerializer(clients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Item APIs
class ItemDataTableAPI(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemDataTableSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
