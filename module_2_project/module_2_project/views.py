from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
# from bs4 import BeautifulSoup
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Vulnes as Vul
# from django import template
# from django.conf import settings
import logging
# import pdfkit
import json


Logging = logging.getLogger('main')
# register = template.Library()

def info(request):
    Logging.info("BOT")
    return render(request, "info.html", {
        "title": "Info"
    })

def home(request):
    Logging.info("BOT")
    return render(request, "home.html", {
        "title": "Home"
    })

def get_new(request):
    Logging.info("BOT")
    return render(request, "get_new.html", {
        "title": "New cve",
    })

def get_critical(request):
    Logging.info("BOT")
    return render(request, "get_critical.html", {
        "title": "Critical cve"
    })

def get_all(request):
    Logging.info("BOT")
    return render(request, "get_all.html", {
        "title": "All cve",
    })

class Vuln(TemplateView):
    Logging.info("BOT")
    template_name = "get_all.html"
    def get(self, request):
        cves = Manage.get_cves()
        cntx = {
            "cves": cves
        }
        # return JsonResponse(cntx, safe=False)
        return render(request, self.template_name, cntx)

class Manage():
    Logging.info("BOT")
    def get_cves():
        req = Vul.objects.all().values()
        return list(req)

def get_new_pdf(request):
    return render(request, "get_new_pdf.html")

def get_critical_pdf(request):
    return render(request, "get_critical_pdf.html")

def get_all_pdf(request):
    return render(request, "get_all_pdf.html")






