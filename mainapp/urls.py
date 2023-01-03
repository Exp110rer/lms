from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import (ContactsView, CoursesView, DocSiteView,
                           IndexView, LoginView, NewsView, NewsPageDetailView)

app_name = MainappConfig.name

urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    path("contacts/", ContactsView.as_view(), name="contacts"),
    path("courses_list/", CoursesView.as_view(), name="courses_list"),
    path("doc_site/", DocSiteView.as_view(), name="doc_site"),
    path("login/", LoginView.as_view(), name="login"),
    path("news/", NewsView.as_view(), name="news"),
    path("news/<int:pk>/", NewsPageDetailView.as_view(), name="news_detail")
]
