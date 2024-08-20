from rest_framework.viewsets import ModelViewSet

from api.models import Product
from api.serializers.product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()