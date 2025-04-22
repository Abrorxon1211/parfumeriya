from rest_framework import serializers
from .models import (
    Mahsulot, Variant, Eslatma, Sharh,
    Blog, Banner, Kategoriya
)


class EslatmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Eslatma
        fields = '__all__'


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class KategoriyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategoriya
        fields = '__all__'


class MahsulotSerializer(serializers.ModelSerializer):
    eslatmalar = EslatmaSerializer(many=True, read_only=True)
    variantlar = VariantSerializer(many=True, read_only=True)
    kategoriya = KategoriyaSerializer(read_only=True)

    class Meta:
        model = Mahsulot
        fields = '__all__'


class SharhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharh
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
