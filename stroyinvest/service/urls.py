from django.urls import path

from service import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='services'),
    path('<slug:service_slug>/', views.ServiceDetailView.as_view(), name='service-detail'),
]
