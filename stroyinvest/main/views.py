from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def documents(request):
    return render(request, 'main/documents.html')

def contacts(request):
    return render(request, 'main/contacts.html')