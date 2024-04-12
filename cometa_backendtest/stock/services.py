from .models import Stock


class StockService:
    @classmethod
    def update_stock(cls, beer_name, new_quantity):
        try:
            stock = Stock.objects.get(beer__name=beer_name)
            stock.quantity = new_quantity
            stock.save()
            return True, None
        except Stock.DoesNotExist:
            return False, "Stock not found for the given beer name"
        except Exception as e:
            return False, str(e)
