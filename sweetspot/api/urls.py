# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CustomerViewSet, CakeViewSet, CartViewSet, OrderViewSet,
    CakeCustomizationViewSet, TokenLogoutView
)

# Set up the router for viewsets
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'cakes', CakeViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'cake-customizations', CakeCustomizationViewSet)

# Include the router URLs and add custom logout endpoints
urlpatterns = [
    path('', include(router.urls)),
    # path('logout/', TokenLogoutView.as_view(), name='customer-logout'), 
]
