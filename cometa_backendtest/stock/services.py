from .models import Stock


class StockService:
    @classmethod
    def update_stock(cls, beer_id, new_quantity):
        try:
            stock = Stock.objects.get(beer_id=beer_id)
            stock.quantity = new_quantity
            stock.save()
            return True, None
        except Stock.DoesNotExist:
            return False, "Stock not found for the given beer ID"
        except Exception as e:
            return False, str(e)
