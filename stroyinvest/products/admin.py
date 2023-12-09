from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe

from ckeditor.widgets import CKEditorWidget

# from products.models import Brand, ProductCategory, Product
from products.models import ProductCategory, Product

# @admin.register(Brand)
# class BrandAdmin(admin.ModelAdmin):
#     list_display = ('title',)


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ('title', 'status', 'price', 'articul', 'brand')
    list_display = ('title', 'status', 'category')
    fields = [
        'photo',
        'photo_preview',
        'title',
        'description',
        'status',
        # 'price',
        # 'old_price',
        # 'articul',
        # 'brand',
        'category',
        'service',
    ]
    search_fields = ('title', 'articul', 'brand')
    readonly_fields = ['photo_preview']

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }

    def photo_preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px;">')

    photo_preview.short_description = 'Фото услуги'
