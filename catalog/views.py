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

from rest_framework import viewsets
from .models import Category, Attribute, Product, ProductAttributeValue
from .serializers import CategorySerializer, AttributeSerializer, ProductSerializer, ProductAttributeValueSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductAttributeValueViewSet(viewsets.ModelViewSet):
    queryset = ProductAttributeValue.objects.all()
    serializer_class = ProductAttributeValueSerializer
