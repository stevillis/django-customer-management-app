from django.shortcuts import render

from accounts.models import *


def home(request):
    return render(request, 'accounts/dashboard.html')


def products(request):
    prds = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': prds})


def customer(request):
    return render(request, 'accounts/customer.html')
