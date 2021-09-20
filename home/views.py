from django.shortcuts import render
from blog.models import BlogPost
from products.models import Product


def index(request):
    """
    A view to return the index page
    """

    blog_home = BlogPost.objects.all().order_by('pk')[:2]
    shop_home = Product.objects.filter(is_holiday=False,
                                       id__in=(7, 24, 13))[:3]

    context = {
        'blog_home': blog_home,
        'shop_home': shop_home,
    }

    return render(request, 'home/index.html', context)
