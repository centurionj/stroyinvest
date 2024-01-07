class TitleListMixin:
    """Миксин для заголовка"""
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleListMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

class TitleDetailMixin:
    """Миксин для заголовка в детальном просмотре"""
    title = 'Стройинвест - '

    def get_context_data(self, **kwargs):
        context = super(TitleDetailMixin, self).get_context_data(**kwargs)
        context['title'] = f'{self.title}{self.object.title}'
        return context