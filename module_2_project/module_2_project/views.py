import io
import os.path

from django.http import HttpResponse, HttpResponseNotFound, JsonResponse, FileResponse
# from bs4 import BeautifulSoup
from django.views.generic import TemplateView
from django.shortcuts import render
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import Vulnes as Vul
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.conf import settings
import logging
import pdfkit
import json

NIST_API = "5a79759a-92b1-4807-9c68-df070b8461ef"

Logging = logging.getLogger('main')

def pdf_down_1(request):
    template_path = "get_all_pdf.html"
    context = {'cves': Manage.get_cves()}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="all.pdf"'
    # View in browser
    # response['Content-Disposition'] = 'filename="all.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error!")
    return response

def pdf_down_2(request):
    template_path = "get_critical_pdf.html"
    context = {'cves2': Manage.get_cves()}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="critical.pdf"'
    # View in browser
    # response['Content-Disposition'] = 'filename="critical.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error!")
    return response

def pdf_down_3(request):
    template_path = "get_new_pdf.html"
    context = {'cves3': Manage.get_cves()}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="new.pdf"'
    # View in browser
    # response['Content-Disposition'] = 'filename="new.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse("Error!")
    return response


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

class Vuln2(TemplateView):
    Logging.info("BOT")
    template_name = "get_critical.html"
    def get(self, request):
        cves = Manage.get_cves()
        cntx2 = {
            "cves2": cves
        }
        return render(request, self.template_name, cntx2)

class Vuln3(TemplateView):
    Logging.info("BOT")
    template_name = "get_new.html"
    def get(self, request):
        cves = Manage.get_cves()
        cntx3 = {
            "cves3": cves
        }
        return render(request, self.template_name, cntx3)

class Manage():
    Logging.info("BOT")
    def get_cves():
        req = Vul.objects.all().values()
        return list(req)






