from django.shortcuts import render


def index(request):
    """The home page for web"""
    return render(request, 'web/home.html')


