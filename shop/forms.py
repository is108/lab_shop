from django import forms

from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('short_title', 'title', 'short_text', 'text', 'img', 'price')
