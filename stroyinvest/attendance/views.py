from django.shortcuts import render


def index(request):
    return render(request, 'services/services.html')

def view(request, service_id):
    return render(request, 'services/service.html')