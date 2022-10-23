from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import json


def getHelloWorld(request):
    response_data = {"name": 'hello world'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def homePage(request):
    response_data = {"name": 'this is home'}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


urlpatterns = [
    path('', homePage),
    path('product/', admin.site.urls),
    path('hello/', getHelloWorld),
]
