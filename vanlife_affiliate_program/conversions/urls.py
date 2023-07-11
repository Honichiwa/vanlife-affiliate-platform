from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path("affiliate/", views.affiliate, name="aff_guide"),
    path("vans/", views.VanListView.as_view(), name="van_list"),
    path("conversion/<slug>", views.ConversionDetailView.as_view(), name="van_detail"),
    path("rvs/", views.RvListView.as_view(), name="rv_list"),
    path("blog/", views.blog, name="blog")
]