from django.db import models
from .beer import Beer


class Stock(models.Model):
    beer = models.OneToOneField(Beer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.beer.name} - Quantity: {self.quantity}"