
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'photo', 'price', 'description']

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter product name'
            }),

            'price': forms.NumberInput(attrs={
                'placeholder': 'Enter price',
                'step': '0.01'
            }),

            'description': forms.Textarea(attrs={
                'placeholder': 'Enter product description',
                'rows': 4
            }),
        }
