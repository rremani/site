from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("INDEX")


def about(request):
    return HttpResponse("ABOUT")


def contact(request):
    return HttpResponse("CONTACT")
