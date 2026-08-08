from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ProductForm
from .models import Product
from .serializers import ProductSerializer


class ProductListView(generic.ListView):
    model = Product
    template_name = "list_products.html"
    context_object_name = "products"


class ProductFormView(generic.FormView):
    template_name = "add_product.html"
    form_class = ProductForm
    success_url = reverse_lazy("create_product")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
