from .models import Order, Item


def get_order_status(order_id):
    try:
        order = Order.objects.get(pk=order_id)
        items = order.items.all().values('name', 'quantity', 'price_per_unit')
        return {
            "created": order.created,
            "paid": order.paid,
            "subtotal": order.subtotal,
            "taxes": order.taxes,
            "discounts": order.discounts,
            "items": list(items)
        }
    except Order.DoesNotExist:
        return None


def create_order(items):
    try:
        order = Order.objects.create()
        for item in items:
            Item.objects.create(
                order=order,
                name=item['name'],
                quantity=item['quantity'],
                price_per_unit=item['price_per_unit']
            )
        return order
    except Exception as e:
        return None


class OrderInteractor:
    def __init__(self):
        self.order_id = None
        self.items = None

    def get_order_status(self, order_id):
        if self.order_id is not None:
            return get_order_status(order_id)
        else:
            return None

    def create_order(self, items):
        if self.items is not None:
            return create_order(items)
        else:
            return None
