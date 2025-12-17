from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ("id","name", "description", "price", "stock", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name", "description")
    list_editable = ("price", "stock")

admin.site.register(Product, ProductAdmin)
