from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'pg_title': 'GISPower-home',
    }
    return render(request, 'home/index.html', context)