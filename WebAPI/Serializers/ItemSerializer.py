from rest_framework import serializers
from adminPanel.models import Item


class ItemDataTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
