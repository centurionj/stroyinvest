from django.contrib import admin

from common.admin_mixin import CKMixin
from news.models import News


@admin.register(News)
class NewsAdmin(CKMixin, admin.ModelAdmin):
    list_display = ('title', 'date')
