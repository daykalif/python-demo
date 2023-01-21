from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'blog2/index.html', {'hello2': 'Hello Bolg222!!!'})
