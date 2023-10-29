from django.urls import path, include

from . import views

app_name = "quotes"

urlpatterns = [
    path("admin/", views.main, name="root"),
    path("", views.main, name="root"),
    path("<int:page>", views.main, name="root_paginate"),
    path("author/<str:author_name>", views.author, name="author_detail"),
    path("tag/<str:tag_name>", views.tag, name="tag_view"),
    path("users/", include("users.urls")),
    path(
        "add_quote/",
        views.add_quote,
        name="add_quote",
    ),
    path(
        "add_author/",
        views.add_author,
        name="add_author",
    ),
]
