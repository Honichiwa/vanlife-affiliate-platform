from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from .models import Conversion
from .forms import ConversionForm

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
    
class ConversionCreateView(LoginRequiredMixin, generic.CreateView):
    model = Conversion
    form_class = ConversionForm
    template_name = 'conversions/conversion_form.html'
    success_url = reverse_lazy('user_conversion_list')

    def get_initial(self) -> Dict[str, Any]:
        initial = super().get_initial()
        c_type = self.request.GET.get('c_type')
        if c_type in ['0', '1']:
            initial['c_type'] = int(c_type)
        initial['owner'] = self.request.user
        return initial
    
    def form_valid(self, form):
        form.instance.owner = self.request.user
        messages.success(self.request, ('Conversion created!'))
        return super().form_valid(form)