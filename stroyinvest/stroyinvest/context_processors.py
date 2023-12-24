from django.conf import settings


def seo_domain(request):
    """Функция возвращает домен для работы SEO"""
    return {'domain': settings.DOMAIN}
