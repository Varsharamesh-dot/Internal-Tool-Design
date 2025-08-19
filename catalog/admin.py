from django.contrib import admin

# Register your models here.
from .models import Category, Attribute, Product, ProductAttributeValue

admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(Product)
admin.site.register(ProductAttributeValue)
