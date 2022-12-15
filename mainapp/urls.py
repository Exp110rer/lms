from django.urls import path

from mainapp.apps import MainappConfig
from mainapp.views import (
    ContactsView,
    CoursesListView,
    DocSiteView,
    IndexView,
    LoginView,
    NewsView,
)

app_name = MainappConfig.name

urlpatterns = [
    path("index/", IndexView.as_view(), name="mainapp_index"),
    path("contacts/", ContactsView.as_view(), name="mainapp_contacts"),
    path("courses_list/", CoursesListView.as_view(), name="mainapp_courses_list"),
    path("doc_site/", DocSiteView.as_view(), name="mainapp_doc_site"),
    path("login/", LoginView.as_view(), name="mainapp_login"),
    path("news/", NewsView.as_view(), name="mainapp_news"),
]
