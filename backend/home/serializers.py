from rest_framework import serializers
from . models import Product


class ProductSrz(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Product
        fields = '__all__'


class ProductDetailSrz(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_url(self, obj):
        return obj.get_absolute_url()
    

class ProductSearchSrz(serializers.Serializer):
    search_item = serializers.CharField(required=False)