from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contacts', views.contacts, name='contacts'),
    path('about-us', views.about_us, name='about-us'),
    path('products', include('products.urls')),
]
