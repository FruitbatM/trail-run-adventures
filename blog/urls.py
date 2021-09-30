from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='basecampblog'),
    path('<int:post_id>/', views.blog_post, name='blog_post'),
    path('add_blog/', views.add_blog, name='add_blog'),
]
