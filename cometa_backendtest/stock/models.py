from django.db import models
from .beer import Beer


class Stock(models.Model):
    DEFAULT_BEER_ID = 1
    beer = models.OneToOneField(Beer, on_delete=models.CASCADE, related_name='stock', default=DEFAULT_BEER_ID)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Stock for {self.beer.name}"
