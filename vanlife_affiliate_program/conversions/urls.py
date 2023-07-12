from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path("affiliate/", views.affiliate, name="aff_guide"),
    path("vans/", views.VanListView.as_view(), name="van_list"),
    path("rvs/", views.RvListView.as_view(), name="rv_list"),
    path('myconversions/', views.UserConversionList.as_view(), name='user_conversion_list'),
    path('myconversions/create/', views.ConversionCreateView.as_view(), name='conversion_create'),
    path('myconversions/delete/<slug>/', views.ConversionDeleteView.as_view(), name='conversion_delete'),
    path('myconversions/update/<slug>/', views.ConversionUpdateView.as_view(), name='conversion_update'),
    path('myconversions/new_gadget/', views.GadgetCreateView.as_view(), name='gadget_create'),
    path('myconversions/edit_gadget/<int:pk>', views.GadgetUpdateDeleteView.as_view(), name='gadget_edit'),
    path("conversion/<slug>/", views.ConversionDetailView.as_view(), name="van_detail"),
]