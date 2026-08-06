from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import ProductForm


class ProductFormView(generic.FormView):
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy('create_product')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
