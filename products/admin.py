from django.contrib import admin
from .models import Product

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'low_stock_warning')

    def low_stock_warning(self, obj):
        if obj.stock < 5:
            return "⚠️ Low!"
        return "✅ OK"
    low_stock_warning.short_description = 'Stock Status'

    search_fields = ('name',)
    fields = ('name', 'image', 'price', 'stock', 'short_description', 'product_description')