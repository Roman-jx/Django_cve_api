from django.conf.urls.static import *
from django.conf.urls import *
from django.contrib import admin
from django.urls import path
from . import views, settings
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', info, name="info"),
    path('', home, name="home"),
    path('get/new/', get_new, name="get_new"),
    path('get/critical', get_critical, name="get_critical"),
    path('get/all', get_all, name="get_all")
]
urlpatterns += staticfiles_urlpatterns()

