from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
import logging
import datetime
import pdfkit


Logging = logging.getLogger('main')
NIST_API_KEY = "5a79759a-92b1-4807-9c68-df070b8461ef"

def info(request):
    Logging.info("BOT")
    return render(request, "info.html", {"title": "Info"})

def home(request):
    Logging.info("BOT")
    return render(request, "home.html", {"title": "Home"})

def get_new(request):
    Logging.info("BOT")
    return render(request, "get_new.html", {"title": "New cve"})

def get_critical(request):
    Logging.info("BOT")
    return render(request, "get_critical.html", {"title": "Critical cve"})

def get_all(request):
    Logging.info("BOT")
    return render(request, "get_all.html", {"title": "All cve"})

# def get
