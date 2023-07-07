from django.contrib import admin
from django.urls import path
from . views import home, about, affiliate, van_list, rv_list, blog

urlpatterns = [
    path('', home, name="home"),
    path('about/', about, name="about"),
    path("affiliate/", affiliate, name="aff_guide"),
    path("vans/", van_list, name="van_list"),
    path("rvs/", rv_list, name="rv_list"),
    path("blog/", blog, name="blog")
]