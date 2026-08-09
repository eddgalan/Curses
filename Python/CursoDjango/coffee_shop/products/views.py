from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductListView(generic.ListView):
    model = Product
    template_name = "list_products.html"
    context_object_name = "products"


class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
