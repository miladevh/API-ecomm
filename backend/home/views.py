from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSrz, ProductDetailSrz, ProductSearchSrz
from rest_framework import status
from django.shortcuts import get_object_or_404



class HomePageView(APIView):
    def get(self, request):
        products = Product.objects.all()
        ser_data = ProductSrz(instance=products, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    


class ProductDetailView(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        ser_data = ProductDetailSrz(instance=product)
        return Response(ser_data.data)
    

class ProductSearchView(APIView):
    def post(self, request):
        ser_data = ProductSearchSrz(data=request.POST)
        if ser_data.is_valid():
            search_item = ser_data.validated_data.get('search_item', '')
            products = Product.objects.filter(available=True, name__contains= search_item)
            if products:
                result = ProductDetailSrz(products, many=True)
                return Response(result.data, status=status.HTTP_200_OK)
            return Response({'message': 'products not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(ser_data.errors, status=status.HTTP_400_BAD_REQUEST)
