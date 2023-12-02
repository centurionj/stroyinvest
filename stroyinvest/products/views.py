from django.shortcuts import render


def index(request):
    return render(request, 'products/products.html')

def view(request, product_id):
    return render(request, 'products/product.html')