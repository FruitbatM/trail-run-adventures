from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'sku',
                  'category', 'price',
                  'rating', 'image',
                  )
    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        labels = {
            'name': 'Product Name *',
            'description': 'Description *',
            'sku': 'SKU *',
            'category': 'Category *',
            'price': 'Price(€) *',
            'rating': 'Rating(0-5)',
            'image': 'Image',
        }

        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-1'


class HolidayForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'duration', 'header_paragraph',
                  'holiday_header_image', 'header_paragraph',
                  'distance', 'level','start_date', 'end_date',
                  'overview_paragraph_1', 'running_days', 'image_1', 'image_2',
                  )
    holiday_header_image = forms.ImageField(label='Header Image', required=True)
    image_1 = forms.ImageField(label='Header Image', required=False)
    image_2 = forms.ImageField(label='Header Image', required=False)
    duration = forms.IntegerField(required=True)

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
            'start_date': 'Start date *',
            'end_date': 'End date *',
            'overview_paragraph_1': 'Overview paragraph',
            'image_url': 'Image URL',
            'running_days': 'Running days',
            'image_1': 'Image',
            'image_2': 'Image',
        }
        
        print(labels)

        for field in self.fields:
            self.fields[field].label = labels[field]

        self.fields['header_paragraph'].widget.attrs['rows'] = 2
        self.fields['price'].widget.attrs['min'] = 500
        self.fields['price'].widget.attrs['max'] = 3500
