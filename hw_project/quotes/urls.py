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
]
