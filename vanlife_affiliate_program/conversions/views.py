from typing import Any
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from .models import Conversion

def home(request):
    return render(request, 'conversions/home.html')

def about(request):
    return render(request, 'conversions/about.html')

def affiliate(request):
    return render(request, 'conversions/aff_guide.html')

class VanListView(generic.ListView):
    model = Conversion
    template_name = 'conversions/van_list.html'
    context_object_name = 'conversions'

class RvListView(generic.ListView):
    model = Conversion
    template_name = 'conversions/rv_list.html'
    context_object_name = 'conversions'

class ConversionDetailView(generic.DetailView):
    model = Conversion
    template_name = 'conversions/conversion_detail.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

class UserConversionList(LoginRequiredMixin, generic.ListView):
    model = Conversion
    template_name = 'conversions/user_conversion_list.html'
    context_object_name = 'conversions' 

    def get_queryset(self) -> QuerySet[Any]:
        qs = super().get_queryset()
        qs = qs.filter(owner=self.request.user)
        return qs