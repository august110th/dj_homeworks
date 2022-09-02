from django.contrib import admin
from .models import StockProduct, Stock, Product


class StockProductInline(admin.TabularInline):
    model = StockProduct
    extra = 1


@admin.register(Product)
class Product(admin.ModelAdmin):
    inlines = [StockProductInline]


@admin.register(Stock)
class Stock(admin.ModelAdmin):
    inlines = [StockProductInline]
