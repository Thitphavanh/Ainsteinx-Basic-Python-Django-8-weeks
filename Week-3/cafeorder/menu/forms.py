from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'name', 'description',
                  'price', 'is_available']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'w-full border rounded p-2'}),
            'price': forms.NumberInput(
                attrs={'class': 'w-full border rounded p-2'}),
        }
