from PIL import Image

from django.urls import reverse


class ModelMixin:
    url_name = None

    def get_absolute_url(self):
        return reverse(self.url_name, args=[self.slug])

    def _image_save(self, *args, **kwargs):
        max_width = 1080

        filepath = self.photo.path
        width = self.photo.width
        height = self.photo.height

        if width > max_width:
            img = Image.open(filepath)
            new_height = int((height / width) * max_width)
            img = img.resize((max_width, new_height), Image.LANCZOS)
            img.save(filepath)
