from .models import Stock, Beer


class StockService:
    @classmethod
    def update_stock(cls, beer_name, new_quantity):
        try:
            stock = Stock.objects.get(beer__name=beer_name)
            if stock.quantity - new_quantity < 0:
                return False, "Not enough stock available"
            else:
                stock.quantity += new_quantity
                beer = Beer.objects.get(id=stock.beer.id)
                beer.quantity += new_quantity
            stock.save()
            beer.save()
            return True, None
        except Stock.DoesNotExist:
            return False, "Stock not found for the given beer name"
        except Exception as e:
            return False, str(e)
