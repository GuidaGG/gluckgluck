from django.shortcuts import render
from django.http import HttpResponse
from .models import Section, Text, Image, Page, Event
from itertools import chain


# Create your views here.
def get_page(page_name):
    images = Image.objects.filter(page__title=page_name)
    text = Text.objects.filter(page__title=page_name)
    sections = sorted(
        chain(images, text), key=lambda section: section.order)

    return sections

def get_events():
    events = Event.objects.all()
    return events

def index(request):
    try:
        sections =  get_page('GluckGluck')
        events = get_events()
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'index.html', {'sections' : sections, 'events' : events})

def impressum(request):
    try:
        sections = get_page('Impressum')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'functional.html', {'sections' : sections})

def datenschutzerklarung(request):
    try:
        sections = get_page('Datenschutzerklarung')
    except Section.DoesNotExist:
        raise Http404("Content does not exist")
    return render(request, 'functional.html', {'sections' : sections})
