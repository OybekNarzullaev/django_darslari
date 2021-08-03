from django.shortcuts import render
from django.http import HttpResponse
from . import models


def hello(request):
    mevalar = models.Meva.objects.all()
    return render(request, 'index.html', {'mevalar': mevalar})


def goodbye(request):
    return HttpResponse("Xayr")


