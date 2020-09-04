from django.shortcuts import render

def index(request):
    """The home page for amsite"""
    return render(request, 'startsite/home.html')