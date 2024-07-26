from django.views.generic import TemplateView
from article.models import Publication


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.all(),
        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publications_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publications_pk)
        }
        return context


class AboutView(TemplateView):
    template_name = 'about.html'
