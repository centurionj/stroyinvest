from django.urls import path, include

from main.views import IndexView, contacts, about_us

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),
    path('about-us/', about_us, name='about-us'),

    path('', include('seo.urls')),
]
