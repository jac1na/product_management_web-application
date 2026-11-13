

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm



@login_required
def dashboard(request):

    products = Product.objects.all().order_by('-id')

    return render(request, 'seller/dashboard.html', {
        'products': products
    })


@login_required
def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductForm()

    return render(request, 'seller/product_form.html', {
        'form': form,
        'title': 'Add New Product'
    })


@login_required
def product_update(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            request.FILES,
            instance=product
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductForm(instance=product)

    return render(request, 'seller/product_form.html', {
        'form': form,
        'title': 'Edit Product'
    })


@login_required
def product_delete(request, pk):

    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        product.delete()

    return redirect('dashboard')
