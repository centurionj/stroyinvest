from django.urls import path

from seo.views import RobotsTxtView, SitemapView

urlpatterns = [
    path('robots.txt', RobotsTxtView.as_view(), name='robots'),
    path('sitemap.xml', SitemapView.as_view(), name='sitemap')
]
