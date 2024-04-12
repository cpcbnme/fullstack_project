from stock.services import StockService
from .models import Order, OrderItem
from stock.models import Stock
from django.db import transaction


class OrderService:
    @classmethod
    @transaction.atomic
    def create_order(cls, items):
        order = Order.objects.create()
        subtotal = 0

        for item_data in items:
            name = item_data['name']
            quantity = item_data['quantity']
            price_per_unit = cls.get_price_for_item(name)
            total = quantity * price_per_unit
            OrderItem.objects.create(order=order, name=name, price_per_unit=price_per_unit, quantity=quantity)
            subtotal += total
            # we will update the stock
            success, error = StockService.update_stock(name, -quantity)
            if not success:
                raise Exception(f"Failed to update stock for {name}: {error}")

        order.subtotal = subtotal
        order.save()

        return order

    @staticmethod
    def get_price_for_item(name):
        beers = Stock.objects.filter(beer__name=name)
        if beers.exists():
            return beers.first().beer.price
