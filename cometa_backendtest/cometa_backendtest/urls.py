from rest_framework.routers import DefaultRouter
from stock.adapters import BeerViewSet, StockListView
from orders.adapters import OrderViewSet

router = DefaultRouter()
router.register(r'beers', BeerViewSet, basename='beer')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'stock', StockListView, basename='stock')

urlpatterns = router.urls
