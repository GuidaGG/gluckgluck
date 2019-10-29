from django.shortcuts import render
from django.http import HttpResponse
from .models import Section

# Create your views here.

def index(request):
    try:
        sections = Section.objects.filter(page__title='GluckGluck')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'index.html', {'sections' : sections})

def impressum(request):
    try:
        sections = Section.objects.filter(page__title='Impressum')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'functional.html', {'sections' : sections})

def datenschutzerklarung(request):
    try:
        sections = Section.objects.filter(page__title='Datenschutzerklärung')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'functional.html', {'sections' : sections})
