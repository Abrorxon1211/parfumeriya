from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('mahsulotlar', MahsulotViewSet)
router.register('variantlar', VariantViewSet)
router.register('eslatmalar', EslatmaViewSet)
router.register('kategoriya', KategoriyaViewSet)
router.register('sharhlar', SharhViewSet)
router.register('bloglar', BlogViewSet)
router.register('bannerlar', BannerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
