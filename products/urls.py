from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('holidays/', views.holidays, name='holidays'),
    path('holidays/<int:holiday_id>/', views.holiday_detail,
         name='holiday_detail'),
]
