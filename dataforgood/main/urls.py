from django.urls import path

from . import views


urlpatterns = [
    # ex: /main/
    path("", views.index, name="index"),
    # ex: /main/12341/
    path("dataandvisualize/", views.dataandvisualize, name="dataandvisualize"),
    # ex: /main/about_us
    path("aboutus/", views.aboutus, name="aboutus"),
    # ex: /main/resources
    path("resources/", views.resources, name="resources"),
    path("download-memo/", views.download_memo, name="download_memo"),
]
