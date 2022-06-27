from django.conf.urls.static import *
from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from . import views, settings
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import Vuln

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info, name="info"),
    path('', home, name="home"),
    path('get/new/', Vuln3.as_view(), name="get_new"),
    path('get/critical/', Vuln2.as_view(), name="get_critical"),
    path('get/all/', Vuln.as_view(), name="get_all"),
    path('get/new/pdf/', pdf_down_3, name="get_new_pdf"),
    path('get/critical/pdf/', pdf_down_2, name="get_critical_pdf"),
    path('get/all/pdf/', pdf_down_1, name="get_all_pdf"),
]
urlpatterns += staticfiles_urlpatterns()

