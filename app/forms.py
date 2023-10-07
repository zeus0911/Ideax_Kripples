from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Title"}))
    description = forms.CharField(widget=forms.TextInput(attrs={"placeholder" : "Description"}))

    class Meta:
        model = Product
        fields = ['title', 'category', 'vendor', 'image', 'description', 'specifications', 'tags', 'product_status', 'featured', 'sku', 'date','file']

