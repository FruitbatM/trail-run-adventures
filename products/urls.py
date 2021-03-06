from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('holidays/', views.holidays, name='holidays'),
    path('holidays/<int:holiday_id>/', views.holiday_detail,
         name='holiday_detail'),
    path('add/', views.add_product, name='add_product'),
    path('holidays/add/', views.add_holiday, name='add_holiday'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('holidays/edit/<int:holiday_id>/', views.edit_holiday,
         name='edit_holiday'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('holidays/delete/<int:holiday_id>/', views.delete_holiday,
         name='delete_holiday'),
]
