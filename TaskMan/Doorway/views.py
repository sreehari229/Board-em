from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from dateutil.relativedelta import relativedelta
import datetime
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
        'signuptrue' : True,
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
    
    return render(request, 'Doorway/login_signup.html', data)

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
                email_obj = UserEmailVerification.objects.get(user=user)
                if email_obj.email_is_verified:
                    login(request, user)
                    return redirect('acc-page')
                else:
                    messages.warning(request, "Email not verified. Please verify your email and then login.")
                    return redirect('login')
            else:
                messages.error(request, "Username/Password is incorrect. Please type in the correct credentials to login.")
                return redirect('login')
            
        return render(request, 'Doorway/login_signup.html')


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
    

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        
        if not User.objects.filter(email=email).first():
            messages.success(request, 'No user found with this email. Try again with a different email.')
            return redirect('forgot_password')
        
        user_obj = User.objects.get(email=email)
        token = str(uuid.uuid4())
        fgp_obj= UserForgotPassword.objects.create(user = user_obj)
        fgp_obj.forget_password_token = token
        fgp_obj.save()
        send_forget_password_mail(user_obj.email , token)
        messages.success(request, 'A Forgot password email has been sent. Please reset your password and login.')
        return redirect('index')
    
    return render(request, "Doorway/PasswordReset/forgot_password.html")


def password_reset(request , token):
    try:
        fgp_obj = UserForgotPassword.objects.filter(forget_password_token = token).first()
        user_id = fgp_obj.user.id
        
        token_creation_time = fgp_obj.created_at
        token_expiration_time = token_creation_time + relativedelta(minutes=20)
        if datetime.datetime.now(datetime.timezone.utc) > token_expiration_time:
            print("Token Expired")
            messages.info(request, "Token has expired, Please create a new token by re entering the details in Forgot-Password page.")
            return redirect('forgot_password')
        
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            
                        
            if user_id is  None:
                messages.success(request, 'No user id found.')
                return redirect(f'/password-reset/{token}/')
                
            
            if  new_password != confirm_password:
                messages.success(request, 'both should  be equal.')
                return redirect(f'/password-reset/{token}/')
                         
            #More Validations to be added
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            messages.success(request, "Password Reset Completed, Please login and continue.")
            return redirect('login')
            
    except Exception as e:
        print(e)
    return render(request , "Doorway/PasswordReset/change_password.html")