from django.forms import ModelForm
from main.models import ProductakhorModel

class ProductForm(ModelForm):
    class Meta:
        model = ProductakhorModel
        fields = ['name', 'price', 'description', 'image', 'quantity']

