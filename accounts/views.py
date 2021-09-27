from django.shortcuts import render, redirect

from accounts.forms import OrderForm
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


def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(pk=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}

    return render(request, 'accounts/order_form.html', context)
