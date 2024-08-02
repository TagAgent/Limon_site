from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from article.models import Publication


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = {
            'publication_list': Publication.objects.filter(is_active=True),
        }
        return context


class PublicationDetailView(TemplateView):
    template_name = 'publication-detail.html'

    def get_context_data(self, **kwargs):
        publication_pk = kwargs['pk']
        context = {
            'publication': Publication.objects.get(id=publication_pk)
        }
        return context


class CreateCommentView(View):

    def post(self, request, *args, **kwargs):
        publication_pk = kwargs['pk']
        publication = Publication.objects.filter(id=publication_pk)
        render(
            request,
            'publication-detail.html',
            {'publication': Publication.objects.get(id=publication_pk)},
        )


class AboutView(TemplateView):
    template_name = 'about.html'
