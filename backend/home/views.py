from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSrz
from rest_framework import status



class HomePageView(APIView):
    def get(self, request):
        products = Product.objects.all()
        ser_data = ProductSrz(instance=products, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK)