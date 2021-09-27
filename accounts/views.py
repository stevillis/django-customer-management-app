from django.shortcuts import render

from accounts.models import *


def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_customers = customers.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders': orders,
        'customers': customers,
        'total_orders': total_orders,
        'total_customers': total_customers,
        'delivered': delivered,
        'pending': pending,
    }

    return render(request, 'accounts/dashboard.html', context)


def products(request):
    prds = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': prds})


def customer(request, pk):
    ctm = Customer.objects.get(pk=pk)

    orders = ctm.order_set.all()
    total_orders = ctm.order_set.count()

    context = {
        'customer': ctm,
        'orders': orders,
        'total_orders': total_orders,
    }

    return render(request, 'accounts/customer.html', context)
