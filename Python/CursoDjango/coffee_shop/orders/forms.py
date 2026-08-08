from django import forms

from products.models import Product


class OrderItemForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.filter(available=True),
        widget=forms.HiddenInput,
    )
