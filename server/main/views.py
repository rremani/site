from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'main/index.html', {'title': 'Hypothizer Labs'})


def about(request):
    return HttpResponse("ABOUT")


def contact(request):
    return HttpResponse("CONTACT")
