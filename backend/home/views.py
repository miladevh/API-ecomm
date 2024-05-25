from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ProductSrz, ProductDetailSrz, ProductSearchSrz, CommentSrz
from rest_framework import status
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema, OpenApiResponse



class HomePageView(APIView):

    # Documentation
    """
        description:show all Product
        parameters:none
        url: / (home page)
    """
    @extend_schema(
        description="show all Product",
        responses={
            200: OpenApiResponse(
                response=ProductSrz(many=True),
                description="a list of products"
            )
        }
    )

    def get(self, request):
        products = Product.objects.all()
        ser_data = ProductSrz(instance=products, many=True)
        return Response(ser_data.data, status=status.HTTP_200_OK,)
    

class ProductDetailView(APIView):

    # Documentation
    '''
    description: Show details of a product
    parameters: (The primary key of the product) name=pk , type=int, required=True
    url: /product/<int:pk>/
    '''
    @extend_schema(
        description="Show details of a product",
        responses={
            200: OpenApiResponse(
                response= ProductDetailSrz,
                description='a list of product detail by comments'
            )
        }
    )

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        ser_data = ProductDetailSrz(instance=product)
        return Response(ser_data.data, status=status.HTTP_200_OK)
    

class ProductSearchView(APIView):
    # Documenation
    """
    description: Search for products by name
    parameters: none
    url: /product/search/
    """
    @extend_schema(
        description="Search for products by name",
        request=ProductSearchSrz,
        responses={
            200: OpenApiResponse(
                response=ProductDetailSrz(many=True),
                description="A list of products matching the search criteria"
            ),
            404: OpenApiResponse(
                response={"message": "Products not found"},
                description="No products found matching the search criteria"
            ),
            400: OpenApiResponse(
                response={"detail": "Invalid input data"},
                description="Invalid input data"
            ),
        }
    )
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



class CommentCreateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    # Documentation
    """
    description: create new comment for a product
    parameters: (The primary key of the product) name=pk , type=int, required=True
    url: /comment/<int:pk>/create/
    """
    @extend_schema(
        description="create new comment for a product",
        request=CommentSrz,
        responses={
            200: OpenApiResponse(
                response=ProductDetailSrz,
                description="a list of product detail by comments"
            )
        }
    )
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        ser_data = CommentSrz(data=request.POST)
        if ser_data.is_valid():
            ser_data.save(user=request.user, product=product)
            result = ProductDetailSrz(instance=product)
            return Response(result.data)