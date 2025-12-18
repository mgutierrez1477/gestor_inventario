from rest_framework import serializers
from .models import Product

#el serializer es un convierte nuestros modelos django a modelos json para las api
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "created_at"
        ]

        read_only_fields = ("id", "created_at")