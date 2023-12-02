from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='services'),
    path('<int:service_id>', views.view, name='service'),
]
