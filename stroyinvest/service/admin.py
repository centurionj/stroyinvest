from django.contrib import admin

from service.models import Icon, Service


@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ('icon', )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('icon', 'description', )