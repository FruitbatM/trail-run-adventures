from django.contrib import admin
from .models import Product, Category, Level, Itinerary, ItineraryDay


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Level)
admin.site.register(Itinerary)
admin.site.register(ItineraryDay)
