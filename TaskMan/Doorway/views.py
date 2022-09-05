from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        
    }
    return render(request, 'Doorway/index_page.html', data)

