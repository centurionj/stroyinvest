from django.urls import path, include

from main.views import IndexView, contacts, about_us, favicon_view

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about-us/', about_us, name='about-us'),
    path('favicon.ico', favicon_view, name='favicon'),

    path('', include('seo.urls')),
]
