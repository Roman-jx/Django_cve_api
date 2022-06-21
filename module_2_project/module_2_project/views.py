from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import logging

Logging = logging.getLogger('main')

def info(request):
    Logging.info("BOT")
    return render(request, "info.html", {"title": "Info"})

def home(request):
    Logging.info("BOT")
    return render(request, "home.html", {"title": "Home"})
