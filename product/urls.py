from django.urls import path
from .views import addProduct, showProduct, create_checkout_session, success_view, cancel_view,webhook

urlpatterns = [
    path('addProduct', addProduct, name='addProduct'),
    path('showProduct', showProduct, name='showProduct'),
    path('payment/<int:pk>', create_checkout_session, name='payment'),
    path('success', success_view, name='success'),
    path('cancel', cancel_view, name='cancel'),
    path('webhook/', webhook, name='webhook')
]