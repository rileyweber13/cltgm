"""cltgm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from cltgm import views

urlpatterns = [
    url(r'^send-email/', views.send_email, name='send-email'),
    url(r'^$', views.home, name='home'),
    url(r'^what-is-dnd/', views.what_is_dnd, name='what-is-dnd'),
    url(r'^pricing/', views.pricing, name='pricing'),
    url(r'^for-parents/', views.for_parents, name='for-parents'),
    url(r'^contact-me/', views.contact_me, name='contact-me'),
    url(r'^404/', views.not_found, name='404'),
    url(r'^admin/', admin.site.urls, name='admin'),
]
