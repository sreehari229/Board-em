from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .utils import *
import uuid

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
            print(firstName,lastName,email,username)

            if User.objects.filter(username=username):
                messages.error(request, "Username already exists! Please try other username")
                return redirect('signup')

            if User.objects.filter(email=email):
                messages.error(request, "Email already exists! Try again with a different email")
                return redirect('signup')

            if len(username) > 25:
                messages.error(request, "Length of username is greater than 25 characters.")
                return redirect('signup')

            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = firstName
            myuser.last_name = lastName
            myuser.save()
            
            verification_object = UserEmailVerification.objects.create(
                user = myuser,
                email_token = str(uuid.uuid4()),
            )
            send_email_token(email, verification_object.email_token)
            messages.info(request, f"An email has been sent to {email}, please verify your email.")
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
                #Add a condition for email verification. Only if email is verified user will be able to login.
                login(request, user)
                return redirect('acc-page')
            else:
                messages.error(request, "Username/Password is incorrect. Please type in the correct credentials to login.")
                return redirect('login')
            
        return render(request, 'Doorway/login_page.html')

@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')


def email_verification(request, token):
    try:
        obj = UserEmailVerification.objects.get(email_token = token)
        obj.email_is_verified = True
        obj.save()
        messages.success(request, "Your email has been verified. Please login and continue.")
        return redirect('login')
    
    except Exception as e:
        messages.error(request, "Invalid token, please verify using the right token.")
        return redirect('login')