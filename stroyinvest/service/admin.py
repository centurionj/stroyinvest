from django.contrib import admin
from django.utils.html import format_html

from service.models import Icon, Service
from common.admin_mixin import ImagePreviewMixin, IconDisplayMixin, CKMixin


@admin.register(Icon)
class IconAdmin(IconDisplayMixin, admin.ModelAdmin):
    list_display = ('title', 'display_icon',)


@admin.register(Service)
class ServiceAdmin(ImagePreviewMixin, CKMixin, IconDisplayMixin, admin.ModelAdmin):
    list_display = ('display_icon', 'title',)
    fields = ['photo', 'image_preview', 'icon', 'display_icon', 'title', 'description', ]
    readonly_fields = ['display_icon', 'image_preview']

    def display_icon(self, obj):
        return format_html(f'{obj.icon.icon}')
