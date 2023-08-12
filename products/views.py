from django.shortcuts import render
from rest_framework.views import APIView
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response


class ProductsListView(APIView):
    products = Product.objects.all()
    def get(self,request):
        ser_data = ProductSerializer(instance=self.products,many=True)
        return Response(ser_data.data,status=200)