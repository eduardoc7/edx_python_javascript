from django.urls import path

from . import views

app_name = 'wiki'
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.show_page, name="show"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create")
]
