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
    path('get/new/', get_new, name="get_new"),
    path('get/critical/', get_critical, name="get_critical"),
    path('get/all/', Vuln.as_view(), name="get_all"),
    path('get/new/pdf/', get_new_pdf, name="get_new_pdf"),
    path('get/critical/pdf/', get_critical_pdf, name="get_critical_pdf"),
    path('get/all/pdf/', get_all_pdf, name="get_all_pdf"),

    # path('get/all/cve/', get_all_content, name="get_all_content"),
    # path('get/new/cve/', get_new_content, name="get_new_content"),
]
urlpatterns += staticfiles_urlpatterns()

