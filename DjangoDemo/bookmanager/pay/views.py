from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.
def order(request):
    return HttpResponse('pay')
