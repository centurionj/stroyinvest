from django.contrib import admin

from customers.models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')
