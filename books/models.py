# books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, default='Unknown Author')  # Ensure this is a CharField
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)  # Ensure this is an IntegerField
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title