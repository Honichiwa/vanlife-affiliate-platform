from typing import Any, Dict
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.query import QuerySet
from .models import Conversion, Gadget, ConversionSocial
from .forms import ConversionForm, GadgetForm, ConversionSocialForm
from urllib.parse import urlparse

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
    

class ConversionDeleteView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.DeleteView
    ):
    model = Conversion
    template_name = 'conversions/user_conversion_delete.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

    def test_func(self) -> bool | None:
        obj = self.get_object()
        return obj.owner == self.request.user
    
    def get_success_url(self) -> str:
        messages.success(self.request, ('Conversion Deleted!'))
        return reverse('user_conversion_list')
    

class ConversionUpdateView(
    LoginRequiredMixin,
    UserPassesTestMixin,
    generic.UpdateView
    ):

    model = Conversion
    form_class = ConversionForm
    template_name = 'conversions/conversion_form.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
            context = super().get_context_data(**kwargs)
            context['update'] = True
            return context

    def test_func(self):
        obj = self.get_object()
        return obj.owner == self.request.user
    
    def get_success_url(self) -> str:
        messages.success(self.request, ('Conversion Updated!'))
        return reverse('user_conversion_list')
    

class GadgetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Gadget
    form_class = GadgetForm
    template_name = 'conversions/gadget_form.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            next_path = urlparse(next_url).path
            return next_path
        else:
            return reverse('user_conversion_list')
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['conversion'] = self.conversion
        return context

    def get_initial(self) -> Dict[str, Any]:
        self.conversion = get_object_or_404(Conversion, id=self.request.GET.get('conversion_id'))
        initial = super().get_initial()
        initial['conversion'] = self.conversion
        return initial

    def form_valid(self, form):
        form.instance.conversion = self.conversion
        messages.success(self.request, ('Gadget Added!'))
        return super().form_valid(form)

class GadgetUpdateDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Gadget
    form_class = GadgetForm
    template_name = 'conversions/gadget_form.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.conversion.owner == self.request.user

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        gadget = self.get_object()
        gadget.delete()
        messages.success(request, 'Gadget Deleted!')
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.success(self.request, 'Gadget Updated!')
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            next_path = urlparse(next_url).path
            return next_path
        else:
            return reverse('user_conversion_list')


class ConversionSocialCreateView(LoginRequiredMixin, generic.CreateView):
    model = ConversionSocial
    form_class = ConversionSocialForm
    template_name = 'conversions/conversion_social_form.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            next_path = urlparse(next_url).path
            return next_path
        else:
            return reverse('user_conversion_list')
        
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['conversion'] = self.conversion
        return context

    def get_initial(self) -> Dict[str, Any]:
        self.conversion = get_object_or_404(Conversion, id=self.request.GET.get('conversion_id'))
        initial = super().get_initial()
        initial['conversion'] = self.conversion
        return initial

    def form_valid(self, form):
        form.instance.conversion = self.conversion
        messages.success(self.request, ('Social Added!'))
        return super().form_valid(form)

class ConversionSocialUpdateDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = ConversionSocial
    form_class = ConversionSocialForm
    template_name = 'conversions/conversion_social_form.html'
    slug_field = 'conversion_slug'
    slug_url_kwarg = 'slug'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = True
        return context

    def test_func(self):
        obj = self.get_object()
        return obj.conversion.owner == self.request.user

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.delete(request, *args, **kwargs)
        else:
            return super().post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        gadget = self.get_object()
        gadget.delete()
        messages.success(request, 'Social Deleted!')
        return redirect(self.get_success_url())

    def form_valid(self, form):
        messages.success(self.request, 'Social Updated!')
        return super().form_valid(form)

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            next_path = urlparse(next_url).path
            return next_path
        else:
            return reverse('user_conversion_list')