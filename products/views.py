from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.filter(is_holiday=False)

    context = {
        'products': products,
    }

    return render(request, 'products/all_products.html', context)


def product_detail(request, product_id):
    """
    A view to display a single product details
    """

    all_products = Product.objects.filter(is_holiday=False)
    product = get_object_or_404(all_products, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
