from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from service.models import Icon, Service


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_icon',)

    def display_icon(self, obj):
        return format_html(f'{obj.icon}')

    display_icon.short_description = 'Иконка'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('display_icon', 'title', )
    fields = ['photo', 'photo_preview', 'icon', 'display_icon', 'title', 'description', ]
    readonly_fields = ['display_icon', 'photo_preview']

    def display_icon(self, obj):
        return format_html(f'{obj.icon.icon}')

    def photo_preview(self, obj):
        return mark_safe(f'<img src="{obj.photo.url}" style="max-height: 200px;">')

    display_icon.short_description = 'Иконка'
    photo_preview.short_description = 'Фото услуги'
