from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('documents', views.documents, name='documents'),
    path('products', include('products.urls')),
    path('services', include('attendance.urls')),
    path('news', include('news.urls')),
]
