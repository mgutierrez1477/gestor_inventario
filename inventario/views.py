from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Product
from .serializers import ProductSerializer

## ViewSet que provee automáticamente las acciones CRUD (list, create, retrieve, update, destroy)
class ProductViewSet(viewsets.ModelViewSet):
    #Queryset base sobre el que operan todas las acciones (list, retrieve, update, delete)
    queryset = Product.objects.all()
    #Serializer encargado de validar datos y convertir entre JSON y Product
    serializer_class = ProductSerializer
    #permisos
    permission_classes = [IsAuthenticatedOrReadOnly]
