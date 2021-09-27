from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk>/', customer, name='customer'),

    path('create_order/', create_order, name='create_order'),
    path('update_order/<str:pk>/', update_order, name='update_order'),
    path('delete_order/<str:pk>/', delete_order, name='delete_order'),
]
