from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Attribute(models.Model):
    DATA_TYPES = [
        ('str','String'),
        ('int','Integer'),
        ('float','Float'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="attributes")
    name = models.CharField(max_length=100)
    data_type = models.CharField(max_length=10, choices=DATA_TYPES, default='str')
    def __str__(self):
        return f"{self.name} ({self.category.name})"

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f"{self.name} - {self.category.name}"

class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="attribute_values")
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.product.name} - {self.attribute.name}: {self.value}"
