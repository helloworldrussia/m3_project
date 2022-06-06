from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.shortcuts import render

from m3 import get_app_urlpatterns


def workspace(request):
    return render(
    request,
    'm3_workspace.html',
    context={'debug': settings.DEBUG},
    )


urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', workspace),
]

urlpatterns.extend(get_app_urlpatterns())
