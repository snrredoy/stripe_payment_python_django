from django.urls import path
from .views import addProduct, showProduct, create_checkout_session

urlpatterns = [
    path('addProduct', addProduct, name='addProduct'),
    path('showProduct', showProduct, name='showProduct'),
    path('payment/<int:pk>', create_checkout_session, name='payment')
]