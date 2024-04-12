from rest_framework import viewsets, status
from rest_framework.response import Response
from .services import OrderService
from .models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ViewSet):
    def create(self, request):
        items = request.data.get('items', [])
        if not items:
            return Response({'error': 'No items provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            order = OrderService.create_order(items)
            return Response({'order_id': order.id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
