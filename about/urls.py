from django.urls import path
from . import views

urlpatterns = [
    path('', views.our_story, name='our_story'),
    path('', views.our_team, name='our_team'),
    path('', views.contact, name='contact'),
]
