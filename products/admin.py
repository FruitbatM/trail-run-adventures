from django.contrib import admin
from .models import Product, Category, Level, Itinerary, ItineraryDay, Faq


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'sku',
        'category',
        'level',
        'price',
        'rating',
        'image',
        'image_1'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class LevelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ItineraryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ItineraryDayAdmin(admin.ModelAdmin):
    list_display = (
        'itinerary',
    )


class FaqAdmin(admin.ModelAdmin):
    list_display = (
        'holiday',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Level, LevelAdmin)
admin.site.register(Itinerary, ItineraryAdmin)
admin.site.register(ItineraryDay, ItineraryDayAdmin)
admin.site.register(Faq, FaqAdmin)