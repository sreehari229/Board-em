from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index_page(request):
    data = {
        
    }
    return render(request, 'Doorway/index_page.html', data)


def signup_page(request):
    data = {
        'form' : UserCreationForm(),
    }
    
    if request.user.is_authenticated:
        return redirect('acc-page')
    else: 
    
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
            return redirect('login')
    
    return render(request, 'Doorway/signup.html', data)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('acc-page')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('acc-page')
            else:
                #Send a flash message/ notification saying Username/Password is incorrect
                pass
        data = {
            
        }
        return render(request, 'Doorway/login_page.html', data)

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')
