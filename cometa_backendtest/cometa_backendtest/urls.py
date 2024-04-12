from rest_framework.routers import DefaultRouter
from stock.adapters import BeerViewSet
from orders.adapters import OrderViewSet

router = DefaultRouter()
router.register(r'beers', BeerViewSet, basename='beer')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls
