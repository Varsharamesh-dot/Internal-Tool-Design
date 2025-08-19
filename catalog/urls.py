from django.urls import path, include
from .views import product_list
from rest_framework import routers
from .views import CategoryViewSet, AttributeViewSet, ProductViewSet, ProductAttributeValueViewSet

# API router
router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'attributes', AttributeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-values', ProductAttributeValueViewSet)

urlpatterns = [
    path('products/', product_list, name='product_list'),  # Template view
    path('', include(router.urls)),                        # API routes
]

