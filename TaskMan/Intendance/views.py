from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def acc_index_page(request):
    data = {
        
    }
    return render(request, 'Intendance/acc_home.html', data)