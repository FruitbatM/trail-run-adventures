from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Itinerary, ItineraryDay, Faq

from .forms import ProductForm, HolidayForm, ItineraryForm


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
    faq = Faq.objects.filter(holiday=holiday)

    context = {
        'holiday': holiday,
        'itinerary': itinerary,
        'itinerary_day': itinerary_day,
        'faq': faq,
    }

    return render(request, 'products/holiday_detail.html', context)


@login_required
def add_product(request):
    """ A view allowing admin to add a product to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Sorry, only site owners have this permission.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure\
                           the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def add_holiday(request):
    """ A view allowing admin to add a holiday tour to the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Sorry, only site owners have this permission.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        holiday_form = HolidayForm(request.POST, request.FILES)
        itinerary_form = ItineraryForm(request.POST, request.FILES)
        if holiday_form.is_valid() and itinerary_form.is_valid():
            holiday = holiday_form.save(commit=False)
            holiday.is_holiday = True
            holiday.save()
            itinerary = Itinerary.objects.create(holiday=holiday,
                                                 name=holiday.name)
            itinerary.save()
            holiday.save()
            messages.success(request, 'Successfully added holiday tour!')
            return redirect(reverse('holiday_detail', args=[holiday.id]))
        else:
            messages.error(request, 'Failed to add holiday tour. Please ensure \
                           the form is valid.')
    else:
        holiday_form = HolidayForm()
        itinerary_form = ItineraryForm()

    template = 'products/add_holiday.html'
    context = {
        'holiday_form': holiday_form,
        'itinerary_form': itinerary_form
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ A view allowing admin user to edit a product on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Sorry, only site owners have this permission.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'The product was successfully updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update the product. Please\
                                     ensure the form is valid.')

    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
            Sorry, only site owners have this permission.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'{product.name} was successfully deleted!')
    return redirect(reverse('products'))


@login_required
def edit_holiday(request, holiday_id):
    """ A view to allow admin user to edit a holiday tour on the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
             Only site owners can edit holiday tours.')
        return redirect(reverse('home'))
    holiday = get_object_or_404(Product, pk=holiday_id)
    if request.method == 'POST':
        form = HolidayForm(request.POST, request.FILES, instance=holiday)
        if form.is_valid():
            holiday = form.save(commit=False)
            holiday.is_holiday = True
            holiday.save()
            messages.success(request, 'Successfully updated holiday tour!')
            return redirect(reverse('holiday_detail', args=[holiday.id]))
        else:
            messages.error(request, 'Failed to update holiday tour.\
                 Please ensure the form is valid.')
    else:
        form = HolidayForm(instance=holiday)
        messages.info(request, f'You are editing {holiday.name}')

    template = 'products/edit_holiday.html'
    context = {
        'form': form,
        'holiday': holiday,
    }
    return render(request, template, context)


@login_required
def delete_holiday(request, holiday_id):
    """ A view to allow admin user to delete a holiday from the site """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied!\
             Only site owners can delete holiday tours.')
        return redirect(reverse('home'))
    holiday = get_object_or_404(Product, pk=holiday_id)
    holiday.delete()
    messages.info(request, f'{holiday.name} was successfully deleted.')
    return redirect(reverse('holidays'))
