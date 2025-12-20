from django.contrib import admin
from django.urls import path, include
#Documentacion
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
#obtenemos los tokens
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("inventario.urls")),
    #recibe la info del usuario y genera un token
    path('api/token/', obtain_auth_token),
    path('api-auth/', include('rest_framework.urls')),

    #openApi schema
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),

    # swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),

    #redoc
    path('api/redoc/', SpectacularRedocView.as_view(url_name="schema"), name="redoc")
]
