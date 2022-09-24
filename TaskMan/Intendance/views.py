from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required(login_url='login')
def acc_index_page(request):
    data = {
        
    }
    return render(request, 'Intendance/acc_home.html', data)

@login_required(login_url='login')
def profile_page(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            #Show some notification - Your account has been updated
            return redirect('profile')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    data = {
        'u_form':user_form,
        'p_form':profile_form,
    }
    return render(request, 'Intendance/profile_page.html', data)
