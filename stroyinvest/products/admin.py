from django.contrib import admin

from products.models import Brand, ProductCategory, Product


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'price', 'articul', 'brand')
    search_fields = ('title', 'articul', 'brand')
