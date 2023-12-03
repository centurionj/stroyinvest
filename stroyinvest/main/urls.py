from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('documents', views.documents, name='documents'),
    path('contacts', views.contacts, name='contacts'),
    path('products', include('products.urls')),
    path('services', include('attendance.urls')),
    path('news', include('news.urls')),
]
