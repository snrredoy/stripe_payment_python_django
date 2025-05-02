from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

# Create your views here.
def addProduct(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST)
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