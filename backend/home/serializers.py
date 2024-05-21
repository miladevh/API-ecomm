from rest_framework import serializers
from . models import Product


class ProductSrz(serializers.ModelSerializer):

    category = serializers.SlugRelatedField(read_only=True, slug_field='name')
    class Meta:
        model = Product
        fields = '__all__'