from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='basecampblog'),
    path('<int:post_id>/', views.blog_post, name='blog_post'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:post_id>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:post_id>/', views.delete_blog, name='delete_blog'),
]
