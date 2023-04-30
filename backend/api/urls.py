# Url di-mapping dari cfehome/urls.py ke sini, terus dari sini manggil methods di views.py
# cfehome

from django.urls import path

from . import views

urlpatterns = [
    path('', views.api_home)
]