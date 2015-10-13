from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {})

def all(request):
    return render(request, 'all.html', {})

def about(request):
    return render(request, 'about.html', {})
