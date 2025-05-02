from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product, Order
import stripe
from django.conf import settings
from django.http import HttpResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your views here.
def addProduct(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST, request.FILES)
        if productForm.is_valid():
            productForm.save()
            return redirect('showProduct')
        else:
            return redirect('addProduct')
    else:
        productForm = ProductForm()

    context = {
        "productForm": productForm
    }

    return render(request, 'product/addProduct.html', context=context)

def showProduct(request):
    products = Product.objects.all()

    context = {
        "products": products
    }

    return render(request, 'product/showProduct.html', context=context)

def create_checkout_session(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        order = Order.objects.create(product=product, amount=product.price)
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data':{
                        'currency': 'usd',
                        'unit_amount': int(product.price * 100),
                        "product_data":{
                            'name': product.name,
                            'description': product.description,
                            # 'images': [product.image.url] if product.image and hasattr(product.image, 'url') and product.image.url.startswith('http') else ['https://via.placeholder.com/150']
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://127.0.0.1:8000' + 'product/success.html',
            cancel_url='http://127.0.0.1:8000' + 'product/cancel.html',
        )
        order.stripe_checkout_session_id = checkout_session.id
        order.save()
    except Exception as e:
        return HttpResponse(str(e))

    return redirect(checkout_session.url)