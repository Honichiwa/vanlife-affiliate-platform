from django.shortcuts import render
from django.views import generic
from . models import BlogPost

class BlogPostListView(generic.ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    slug_field = 'blog_slug'
    slug_url_kwarg = 'slug'
    context_object_name = 'blog'