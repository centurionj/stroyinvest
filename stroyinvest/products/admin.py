from django.contrib import admin

from products.models import ProductCategory, Product
from common.admin_mixin import ImagePreviewMixin, CKMixin


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(ImagePreviewMixin, CKMixin, admin.ModelAdmin):
    list_display = ('title', 'status', 'category')
    fields = [
        'photo',
        'image_preview',
        'title',
        'description',
        'status',
        'category',
        'services',
    ]
    search_fields = ('title', 'articul')
    readonly_fields = ['image_preview']
