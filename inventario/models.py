from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, verbose_name="Producto")
    description = models.TextField(max_length=300,  blank=False, verbose_name="Descripcion")
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                validators=[MinValueValidator(0)])
    
    stock = models.PositiveIntegerField(verbose_name="Cantidad")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")

    class Meta:
        ordering = ["-created_at", "name"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.name