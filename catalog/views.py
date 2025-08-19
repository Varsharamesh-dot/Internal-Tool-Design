from django.shortcuts import render

# Create your views here.
from .models import Product, ProductAttributeValue

def product_list(request):
    products = Product.objects.all()  
    product_attributes = ProductAttributeValue.objects.all()
    context = {
        'products': products,
        'product_attributes': product_attributes
    }
    return render(request, 'catalog/product_list.html', context)
