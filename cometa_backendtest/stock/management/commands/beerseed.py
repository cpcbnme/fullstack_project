from django.core.management.base import BaseCommand
from datetime import datetime
from stock.models import Stock, Beer


class Command(BaseCommand):
    help = 'Seed database with initial stock data'

    def handle(self, *args, **kwargs):
        # Truncate the Stock table to avoid duplicates
        Stock.objects.all().delete()

        # Create some initial stock data
        initial_stock_data = [
            {"name": "Corona", "price": 115, "quantity": 2},
            {"name": "Quilmes", "price": 120, "quantity": 0},
            {"name": "Club Colombia", "price": 110, "quantity": 3}
        ]

        for beer_data in initial_stock_data:
            beer, _ = Beer.objects.get_or_create(name=beer_data['name'], price=beer_data['price'])
            Stock.objects.create(beer=beer, quantity=beer_data['quantity'], last_updated=datetime.now())

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with initial stock data'))
