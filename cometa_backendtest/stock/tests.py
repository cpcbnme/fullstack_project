from django.test import TestCase, Client
from django.urls import reverse
from .models import Beer, Stock
import json


class UpdateStockInteractorTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_update_stock(self):
        stock_data = {
            "last_updated": "2024-09-10 12:00:00",
            "beers": [
                {"name": "Corona", "price": 115, "quantity": 2},
                {"name": "Quilmes", "price": 120, "quantity": 0},
                {"name": "Club Colombia", "price": 110, "quantity": 3}
            ]
        }

        response = self.client.post(reverse('update_stock'), data=json.dumps(stock_data),
                                    content_type='application/json')

        self.assertEqual(response.status_code, 200)

        stock = Stock.objects.first()
        self.assertEqual(stock.beers.count(), 3)

        corona = Beer.objects.get(name="Corona")
        self.assertEqual(corona.price, 115)
        self.assertEqual(corona.quantity, 2)

        quilmes = Beer.objects.get(name="Quilmes")
        self.assertEqual(quilmes.price, 120)
        self.assertEqual(quilmes.quantity, 0)

        club_colombia = Beer.objects.get(name="Club Colombia")
        self.assertEqual(club_colombia.price, 110)
        self.assertEqual(club_colombia.quantity, 3)
