#Importa el generador automático de rutas.
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

#Crea una instancia del router que genera automáticamente las URLs
router = DefaultRouter()

#Registrar el ViewSet
router.register (
    r"products", #prefijo de las urls
    ProductViewSet, #clase que maneja las operaciones crud
    basename="product" #nombre base para rutas internas
)

#Exponer las URLs
urlpatterns = router.urls
