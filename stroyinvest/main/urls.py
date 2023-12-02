from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', include('products.urls')),
    path('services', include('attendance.urls')),
]
