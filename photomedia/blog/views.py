from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/index.html', data)


# TODO: about, category Paul

# TODO: contact, single-blog Daouda
