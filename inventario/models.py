from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name="Producto")
    description = models.TextField(max_length=300, null=False, blank=False, verbose_name="Descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    stock = models.IntegerField(
        #validar que el stock siempre sea positivo en toda la app
        validators=[MinValueValidator(0)]
    )
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name