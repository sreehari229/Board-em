from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *

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
            messages.success(request, "Your profile has been updated.")
            return redirect('profile')
        
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
        
    data = {
        'u_form':user_form,
        'p_form':profile_form,
    }
    return render(request, 'Intendance/profile_page.html', data)


# project_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True, blank=True)
#     url = models.URLField(null=True, blank=True)
#     group_members = models.ManyToManyField(User, blank=True, related_name="group_members")
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
#     created_date = models.DateField(auto_now_add=True)
#     start_date = models.DateField()
#     duration = models.IntegerField()
#     modified_date = models.DateField(auto_now=True)

@login_required(login_url='login')
def create_project_page(request):
    form = CreateProjectForm()
    if request.method == 'POST':
        print("Create Order Request ------------ ", request.POST)
        name = request.POST.get('name')
        descript = request.POST.get('description')
        url = request.POST.get('url')
        gm = request.POST.get('group_members')
        sd = request.POST.get('start_date')
        dura = request.POST.get('duration')
        usr = request.user
        print(name, descript, url, gm , sd, dura, usr)
        pj = Project.objects.create(
            name=name,
            description=descript,
            url=url,
            created_by=usr,
            start_date=sd,
            duration=dura
        )
        user_usernames = [x.username for x in User.objects.all()]
        user_id = []
        for x in user_usernames:
            user_id.append(int(request.POST.get(x))) if request.POST.get(x) else print("Nothing")
        print(user_id)
        for pkid in user_id:
            print(pkid)
            pj.group_members.add(User.objects.get(id=pkid))
            
    data = {
        'form' : form,
        'users' : User.objects.all()
    }
    return render(request, 'Intendance/create_project.html', data)
