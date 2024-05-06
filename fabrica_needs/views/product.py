from rest_framework.viewsets import ModelViewSet
from fabrica_needs.models import Product
from fabrica_needs.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    