from rest_framework import serializers

from Client.models import Client
from WebAPI.Serializers.CitySerializer import CitySerializer


class ClientDataTableSerializer(serializers.ModelSerializer):
    city = CitySerializer()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'contact_person', 'phone_number', 'mobile_number', 'email', 'city']
