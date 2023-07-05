from django.shortcuts import render

def home(request):
    return render(request, 'conversions/home.html')