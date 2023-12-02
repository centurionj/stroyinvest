from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='products'),
    path('/<int:product_id>', views.view, name='product'),
]
