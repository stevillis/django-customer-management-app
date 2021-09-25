from django.urls import path

from accounts.views import *

urlpatterns = [
    path('', home),
    path('products/', products),
    path('customer/', customer),
]
