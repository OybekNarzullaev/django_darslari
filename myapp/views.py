from django.shortcuts import render
from django.http import HttpResponse


def hello(request):
    names = ['Oybek', 'Shoxzod', 'Madinabonu']
    name = 'Oybek'
    return render(request, 'index.html', {'ism': name, 'ismlar': names})


def goodbye(request):
    return HttpResponse("Xayr")


