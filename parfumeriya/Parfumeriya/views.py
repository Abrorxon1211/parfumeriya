from rest_framework import viewsets
from .models import (
    Mahsulot, Variant, Eslatma, Sharh,
    Blog, Banner, Kategoriya
)
from .serializers import (
    MahsulotSerializer, VariantSerializer, EslatmaSerializer,
    SharhSerializer, BlogSerializer, BannerSerializer, KategoriyaSerializer
)


class MahsulotViewSet(viewsets.ModelViewSet):
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSerializer


class VariantViewSet(viewsets.ModelViewSet):
    queryset = Variant.objects.all()
    serializer_class = VariantSerializer


class EslatmaViewSet(viewsets.ModelViewSet):
    queryset = Eslatma.objects.all()
    serializer_class = EslatmaSerializer


class KategoriyaViewSet(viewsets.ModelViewSet):
    queryset = Kategoriya.objects.all()
    serializer_class = KategoriyaSerializer


class SharhViewSet(viewsets.ModelViewSet):
    queryset = Sharh.objects.all()
    serializer_class = SharhSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
