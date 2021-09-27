from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Itinerary, ItineraryDay

from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries
    """

    products = Product.objects.filter(is_holiday=False)
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera.\
                               Please try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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


def holidays(request):
    """ A view to display all holiday adventures"""

    holidays = Product.objects.filter(is_holiday=True)
    context = {
        'holidays': holidays,
    }

    return render(request, 'products/holidays.html', context)


def holiday_detail(request, holiday_id):
    """
    A view to display a single holiday adventure details page"
    """

    all_holidays = Product.objects.filter(is_holiday=True)
    holiday = get_object_or_404(all_holidays, pk=holiday_id)
    itinerary = Itinerary.objects.get(holiday=holiday)
    itinerary_day = ItineraryDay.objects.filter(itinerary=itinerary)

    context = {
        'holiday': holiday,
        'itinerary': itinerary,
        'itinerary_day': itinerary_day,
    }

    return render(request, 'products/holiday_detail.html', context)


def add_product(request):
    """ A view allowing admin to add a product to the shop """
    product_form = ProductForm(request.POST, request.FILES)
    template = 'products/add_product.html'
    context = {
        'product_form': product_form,
    }

    return render(request, template, context)