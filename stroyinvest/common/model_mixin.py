from django.urls import reverse


class ModelMixin:
    url_name = None

    def get_absolute_url(self):
        return reverse(self.url_name, args=[self.slug])
