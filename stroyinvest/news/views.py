from django.shortcuts import render


def index(request):
    return render(request, 'news/news.html')

def view(request, news_id):
    return render(request, 'news/news_detail.html')