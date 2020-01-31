from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bill = models.FloatField(default=0)
    address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        created_at = self.created_at.strftime('%B %d, %Y | %H:%M')
        return f'{self.user}: {self.bill} at {created_at}'


class OrderItem(models.Model):
    product = models.ForeignKey('stock.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey('order.Order', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.order.bill += self.product.price * self.quantity
        self.order.save()
        super(OrderItem, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.product} (#{self.quantity})'


class Checkout(models.Model):
    order = models.OneToOneField('order.Order', on_delete=models.CASCADE)
    payment_rate = models.FloatField()

    def __str__(self):
        return str(self.order)
