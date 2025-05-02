from django.urls import path
from .views import addProduct, showProduct

urlpatterns = [
    path('addProduct', addProduct, name='addProduct'),
    path('showProduct', showProduct, name='showProduct'),
]