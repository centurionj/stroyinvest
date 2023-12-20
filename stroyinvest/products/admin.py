from django.contrib import admin

# from products.models import Brand, ProductCategory, Product
from products.models import ProductCategory, Product
from common.admin import ImagePreviewMixin, CKMixin


# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('title',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(ImagePreviewMixin, CKMixin, admin.ModelAdmin):
    # list_display = ('title', 'status', 'price', 'articul', 'brand')
    list_display = ('title', 'status', 'category')
    fields = [
        'photo',
        'image_preview',
        'title',
        'description',
        'status',
        # 'price',
        # 'old_price',
        # 'articul',
        # 'brand',
        'category',
        'services',
    ]
    # search_fields = ('title', 'articul', 'brand')
    search_fields = ('title', 'articul')
    readonly_fields = ['image_preview']
