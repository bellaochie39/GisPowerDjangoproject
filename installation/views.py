from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'pg_title': 'GISPower-installation',
    }
    return render(request, 'installation/index.html', context)