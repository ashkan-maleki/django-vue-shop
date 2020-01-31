from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bill = models.FloatField(default=0)
    address = models.CharField(max_length=500)


class OrderItem(models.Model):
    product = models.ForeignKey('stock.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)


class Checkout(models.Model):
    order = models.OneToOneField('order.Order', on_delete=models.CASCADE)
    payment_rate = models.FloatField()
