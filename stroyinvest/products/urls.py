from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductsListView.as_view(), name='products'),
    path('<slug:product_slug>/', views.ProductsDetailView.as_view(), name='product-detail'),
]
