from rest_framework import serializers

from stock import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['name', 'price', 'quantity']
