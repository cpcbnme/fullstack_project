from rest_framework import serializers
from .models import Beer, Stock


class BeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beer
        fields = ['id', 'name', 'price', 'quantity']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['beer', 'quantity', 'last_updated']
