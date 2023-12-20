from django.utils.safestring import mark_safe
from django.db import models
from django.utils.html import format_html

from ckeditor.widgets import CKEditorWidget


class ImagePreviewMixin:
    """Миксин для отображения картинок в админке"""

    def image_preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" style="max-height: 200px;">')

    image_preview.short_description = 'Фотография предпросмотр'


class IconDisplayMixin:
    """Миксин для отображения иконок в админке"""

    def display_icon(self, obj):
        return format_html(f'{obj.icon}')

    display_icon.short_description = 'Иконка'


class CKMixin:
    """Миксин для текстового редактора в админке"""
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
