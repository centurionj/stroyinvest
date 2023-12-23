from django.urls import include, path

from api.v1.customers import urls as urls_customers


urlpatterns = [
    path('customers/', include(urls_customers)),
]
