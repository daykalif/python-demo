from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


class SetSession(View):
    def get(self, request):
        # request.session = SessionStorage
        request.session['name'] = 'itcast'
        return HttpResponse('abc')
