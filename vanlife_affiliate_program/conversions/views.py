from django.shortcuts import render

def home(request):
    return render(request, 'conversions/home.html')

def about(request):
    return render(request, 'conversions/about.html')

def affiliate(request):
    return render(request, 'conversions/aff_guide.html')

def van_list(request):
    return render(request, 'conversions/van_list.html')

def rv_list(request):
    return render(request, 'conversions/rv_list.html')

def blog(request):
    return render(request, 'conversions/blog.html')