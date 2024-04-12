from rest_framework import viewsets
from rest_framework.response import Response
from .models import Beer, Stock
from .serializers import BeerSerializer, StockSerializer


class StockListView(viewsets.ViewSet):
    def list(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)


class BeerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Beer.objects.all()
        serializer = BeerSerializer(queryset, many=True)
        return Response(serializer.data)




