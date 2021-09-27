from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect

from accounts.filters import OrderFilter
from accounts.forms import CreateUserForm, OrderForm
from accounts.models import *


@login_required(login_url='login')
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


@login_required(login_url='login')
def products(request):
    prds = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': prds})


@login_required(login_url='login')
def customer(request, pk):
    ctm = Customer.objects.get(pk=pk)

    orders = ctm.order_set.all()
    total_orders = ctm.order_set.count()

    my_filter = OrderFilter(request.GET, queryset=orders)
    orders = my_filter.qs

    context = {
        'customer': ctm,
        'orders': orders,
        'total_orders': total_orders,
        'my_filter': my_filter,
    }

    return render(request, 'accounts/customer.html', context)


@login_required(login_url='login')
def create_order(request, pk):
    order_form_set = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=1)
    ctm = Customer.objects.get(pk=pk)
    formset = order_form_set(queryset=Order.objects.none(), instance=ctm)

    # form = OrderForm(initial={'customer': ctm})
    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = order_form_set(request.POST, instance=ctm)
        if formset.is_valid():
            formset.save()
            return redirect('home')

    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def delete_order(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('home')

    context = {'order': order}

    return render(request, 'accounts/delete.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # form = UserCreationForm()
        form = CreateUserForm()

        if request.method == 'POST':
            # form = UserCreationForm(request.POST)
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()

                username = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {username}')

                return redirect('login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect!')

    context = {}
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')
