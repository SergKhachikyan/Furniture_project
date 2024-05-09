from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def index(request):

    context = {
        'title': 'home',
        'content': 'main shop page'

    }

    return render(request,'main/index.html', context)
