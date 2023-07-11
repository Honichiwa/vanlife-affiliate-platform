from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("blog/", views.BlogPostListView.as_view(), name="blog"),
    path("blog/<slug>", views.BlogPostDetailView.as_view(), name="blog_detail"),
]