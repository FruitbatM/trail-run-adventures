from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ItineraryDay


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'sku',
                  'category', 'price', 'has_sizes',
                  'rating', 'image',
                  )
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Product Name',
            'description': 'Description *',
            'sku': 'SKU',
            'category': 'Category',
            'price': 'Price(€)',
            'has_sizes': 'Product Size',
            'rating': 'Rating(0-5)',
            'image': 'Image',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        self.fields['category'].choices = friendly_names
        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['description'].widget.attrs['rows'] = 2
        self.fields['price'].widget.attrs['min'] = 0
        self.fields['price'].widget.attrs['max'] = 500
        self.fields['rating'].widget.attrs['min'] = 0
        self.fields['rating'].widget.attrs['max'] = 5


class HolidayForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'duration', 'header_paragraph',
                  'holiday_header_image', 'header_paragraph',
                  'distance', 'level', 'start_date', 'end_date',
                  'overview_paragraph_1', 'running_days', 'image_1', 'image_2',
                  )
    holiday_header_image = forms.ImageField(label='Header Image', required=True)
    image_1 = forms.ImageField(label='Header Image', required=False)
    image_2 = forms.ImageField(label='Header Image', required=False)
    duration = forms.IntegerField(required=True)
    start_date = forms.DateField(required=True)
    end_date = forms.DateField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Holiday Name',
            'price': 'Price(€)',
            'header_paragraph': 'Header paragraph',
            'holiday_header_image': 'Header Image URL',
            'duration': 'Duration (in days)',
            'distance': 'Distance (in km) *',
            'level': 'Dificulty level *',
            'start_date': 'Start date',
            'end_date': 'End date',
            'overview_paragraph_1': 'Overview paragraph',
            'image_url': 'Image URL',
            'running_days': 'Running days',
            'image_1': 'Image',
            'image_2': 'Image',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['header_paragraph'].widget.attrs['rows'] = 2
        self.fields['price'].widget.attrs['min'] = 500
        self.fields['price'].widget.attrs['max'] = 3500


class ItineraryForm(forms.ModelForm):

    class Meta:
        model = ItineraryDay
        fields = (
            'day_1', 'day_1_overview', 'day_1_hotel', 'day_1_data'
            )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        labels = {
            'day_1': 'Day 1',
            'day_1_overview': 'Day 1 Overview',
            'day_1_hotel': 'Day 1 Hotel',
            'day_1_data': 'Day 1 Data',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]
