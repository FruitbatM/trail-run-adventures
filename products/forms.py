from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'sku',
                  'category', 'price',
                  'rating','image',
                  )
    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

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
