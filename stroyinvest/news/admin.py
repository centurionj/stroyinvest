from django.contrib import admin
from django.db import models

from ckeditor.widgets import CKEditorWidget

from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
