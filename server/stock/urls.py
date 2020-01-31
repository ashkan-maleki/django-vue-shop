from django.urls import path, include
from rest_framework import routers

from stock import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)

app_name = 'stock'
urlpatterns = [
    path('', include(router.urls)),
]
