from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView
from mainapp.models import News

# Create your views here.


class IndexView(TemplateView):
    template_name = "mainapp/index.html"


class ContactsView(TemplateView):
    template_name = "mainapp/contacts.html"


class CoursesView(TemplateView):
    template_name = "mainapp/courses.html"


class DocSiteView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LoginView(TemplateView):
    template_name = "mainapp/login.html"


class NewsView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_list"] = News.objects.all()
        return context
    

class NewsPageDetailView(TemplateView):
    template_name = 'mainapp/news_detail.html'

    def get_context_data(self, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        context["news_object"] = get_object_or_404(News, pk = pk)
        return context
    

