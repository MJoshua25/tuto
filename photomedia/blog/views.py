from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from . import models


# Create your views here.

def index(request: HttpRequest) -> HttpResponse:
    data = {
        'articles': models.Article.objects.filter(status=True).order_by('-date_add')[:2]
    }
    return render(request, 'pages/index.html', data)


# TODO: about, category Paul

# TODO: contact, single-blog Daouda

def single(request: HttpRequest, titre_slug: str) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/single-blog.html', data)


def contact(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/contact.html', data)


def about(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/about.html', data)


def category(request: HttpRequest) -> HttpResponse:
    data = {

    }
    return render(request, 'pages/category.html', data)


@login_required
def dashboardView(request):
    return render(request, 'pages/dashboard.html')


def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()

    return render(request, 'pages/register.html', {'form': form})


def loginView(request):
    return render(request, 'pages/login.html')
