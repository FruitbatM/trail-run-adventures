from django import forms
import datetime
from .widgets import CustomClearableFileInput
from .models import Product, Category, ItineraryDay, Itinerary


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
        fields = ('name', 'country', 'price', 'duration', 'header_paragraph',
                  'holiday_header_image', 'header_paragraph',
                  'distance', 'level', 'start_date', 'end_date',
                  'number_of_runners', 'overview_paragraph_1',
                  'overview_paragraph_2', 'running_days', 'min_elavation',
                  'max_elavation', 'elevation_gain', 'route_image',
                  'image_1', 'image_2', 'image_3'
                  )
    holiday_header_image = forms.ImageField(label='Header Image',
                                            required=True)
    image_1 = forms.ImageField(required=True)
    image_2 = forms.ImageField(required=False)
    image_3 = forms.ImageField(required=False)
    route_image = forms.ImageField(required=False)
    duration = forms.IntegerField(required=True)
    distance = forms.IntegerField(required=True)
    number_of_runners = forms.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Holiday Name',
            'country': 'Country',
            'price': 'Price(€)',
            'header_paragraph': 'Header paragraph',
            'holiday_header_image': 'Header Image URL',
            'duration': 'Duration (in days)',
            'distance': 'Distance (in km) *',
            'level': 'Dificulty level *',
            'start_date': 'Start date format Y-m-d',
            'end_date': 'End date format Y-m-d',
            'number_of_runners': 'number_of_runners',
            'overview_paragraph_1': 'Overview paragraph',
            'overview_paragraph_2': 'Overview paragraph',
            'min_elavation': 'max_elavation',
            'max_elavation': 'max_elavation',
            'elevation_gain': 'elevation_gain',
            'route_image': 'route_image',
            'image_url': 'Image URL',
            'running_days': 'Running days',
            'image_1': 'Image',
            'image_2': 'Image',
            'image_3': 'Image',
        }

        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['header_paragraph'].widget.attrs['rows'] = 2
        self.fields['price'].widget.attrs['min'] = 500
        self.fields['price'].widget.attrs['max'] = 3500
        self.fields['start_date'].input_formats = ['%Y-%m-%d']
        self.fields['end_date'].input_formats = ['%Y-%m-%d']


class ItineraryForm(forms.ModelForm):

    class Meta:
        model = ItineraryDay
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
