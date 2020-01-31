from django.shortcuts import render
from rest_framework import viewsets

from stock import models, serializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = models.Product.objects.all().order_by('name')
    serializer_class = serializers.ProductSerializer
