from django.urls import path
from . import views


urlpatterns = [
    path('our-story/', views.our_story, name='our_story'),
    path('our-team/', views.our_team, name='our_team'),
]
