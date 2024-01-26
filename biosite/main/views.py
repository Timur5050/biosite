from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

menu = [{'title': 'Timur Stukan', 'url_name': 'main'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Background', 'url_name': 'background'},
        {'title': 'Contact', 'url_name': 'contact'}]

def index(request):
    data = {
        'title': 'main page',
        'menu': menu,
    }

    t = render_to_string('main/index.html', context=data)
    return HttpResponse(t)