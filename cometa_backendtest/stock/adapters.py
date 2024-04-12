from rest_framework import viewsets
from rest_framework.response import Response
from .models import Beer
from .serializers import BeerSerializer


class BeerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Beer.objects.all()
        serializer = BeerSerializer(queryset, many=True)
        return Response(serializer.data)
