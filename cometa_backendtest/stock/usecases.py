from .models import Beer, Stock


def update_stock(stock_data):
    stock, _ = Stock.objects.get_or_create(pk=1)
    for beer_data in stock_data.get('beers', []):
        beer, _ = Beer.objects.get_or_create(name=beer_data['name'])
        beer.price = beer_data['price']
        beer.quantity = beer_data['quantity']
        beer.save()
        stock.beers.add(beer)
    stock.save()


def get_all_stock():
    stock = Stock.objects.first()
    return {
        "last_updated": stock.last_updated,
        "beers": [
            {
                "name": beer.name,
                "price": beer.price,
                "quantity": beer.quantity
            }
            for beer in stock.beers.all()
        ]
    }


class StockInteractor:
    def __init__(self, stock_data=None):
        self.stock_data = stock_data

    def handle_stock(self):
        if self.stock_data:
            update_stock(self.stock_data)
        return get_all_stock()
