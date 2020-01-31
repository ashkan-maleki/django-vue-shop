from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=300)
    quantity = models.IntegerField()
    price = models.FloatField()

    def __str__(self):
        return f'{self.name}: {self.price}$ (#{self.quantity})'
