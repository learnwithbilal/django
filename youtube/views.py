from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello World!")


def humam(request):
    return HttpResponse("Hello Humam!")


def ali(request):
    return HttpResponse("Hello Ali!")


def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")