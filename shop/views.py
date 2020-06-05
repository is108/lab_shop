from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
import datetime
from django.utils import timezone

from .models import Product
from .forms import ProductForm


def product_info(request, pk):
    product = get_object_or_404(Product, pk = pk)

    return render(request, 'shop/product_info.html', {'product': product})

def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.pub_data = timezone.now()
            product.save()
            return redirect('product_info', pk=product.pk)
    else:
        form = ProductForm()
    return render(request, 'shop/new_product.html', {'form': form})

def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance = product)
        if form.is_valid():
            product = form.save(commit = False)
            product.pub_data = timezone.now()
            product.save()
            return redirect('product_info', pk = product.pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/new_product.html', {'form': form})

def show_products(request):
    products = Product.objects.all()

    return render(request, 'shop/show_products.html', {'products': products})

def search(request):
    if 'search' in request.GET:
        search = request.GET['search']
        products = Product.objects.filter(short_title = search)

        return render(request, 'shop/show_products.html', {'products': products})
