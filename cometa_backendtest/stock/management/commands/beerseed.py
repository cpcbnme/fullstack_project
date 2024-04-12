from django.core.management.base import BaseCommand
from stock.models import Beer


class Command(BaseCommand):
    help = 'Seed database with initial beer data'

    def handle(self, *args, **kwargs):

        Beer.objects.all().delete()

        beers = [
            {
                "name": "Corona",
                "price": 115,
                "quantity": 250
            },
            {
                "name": "Quilmes",
                "price": 120,
                "quantity": 521
            },
            {
                "name": "Club Colombia",
                "price": 110,
                "quantity": 540
            },
            {
                "name": "Heineken",
                "price": 232,
                "quantity": 520
            }
        ]

        for beer_data in beers:
            beer = Beer.objects.create(
                name=beer_data['name'],
                price=beer_data['price'],
                quantity=beer_data['quantity']
            )
            beer.save()

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with beer data'))
