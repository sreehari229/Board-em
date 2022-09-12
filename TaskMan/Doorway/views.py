from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


def index(request):
    data = {
        
    }
    return render(request, 'Doorway/index_page.html', data)


def signup(request):
    data = {
        'form' : UserCreationForm(),
    }
    
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        rePassword = request.POST.get('rePassword')

        if User.objects.filter(username=username):
            #messages.error(request, "Username already exists! Please try other username")
            return redirect('signup')

        if User.objects.filter(email=email):
            #messages.error(request, "Email already exists! Try again with a different email")
            return redirect('signup')

        if len(username) > 25:
            #messages.error(request, "Length of username is greater than 25 characters.")
            return redirect('signup')

        if password != rePassword:
            #messages.error(request, "Password does not match!")
            return redirect('signup')

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
    
    return render(request, 'Doorway/signup.html', data)

def login(request):
    data = {
        
    }
    return render(request, 'Doorway/login_page.html', data)