from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=150, label="Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    price = forms.DecimalField(max_digits=5, decimal_places=2, label="Price")
    available = forms.BooleanField(initial=True, required=False, label="Available")
    photo = forms.ImageField(label="Photo", required=False)

    def save(self):
        Product.objects.create(
            name=self.cleaned_data["name"],
            description=self.cleaned_data["description"],
            price=self.cleaned_data["price"],
            available=self.cleaned_data["available"],
            photo=self.cleaned_data["photo"],
        )
