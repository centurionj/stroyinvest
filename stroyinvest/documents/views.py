from django.views.generic.list import ListView

from documents.models import Document


class DocumentsListView(ListView):
    """Список всех документов"""
    model = Document
    template_name = 'documents/documents.html'
