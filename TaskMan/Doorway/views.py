from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def index(request):
    data = {
        
    }
    return render(request, 'Doorway/index_page.html', data)


def signup(request):
    data = {
        'form' : UserCreationForm(),
    }
    return render(request, 'Doorway/signup.html', data)

def login(request):
    data = {
        
    }
    return render(request, 'Doorway/login_page.html', data)