from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It now is %s.</body></html>"%now
    return HttpResponse(html)