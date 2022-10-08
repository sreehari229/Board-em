from turtle import title
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *

@login_required(login_url='login')
def acc_index_page(request):
    data = {
        'projects_data' : Project.objects.filter(group_members=request.user),    
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
        for pkid in user_id:
            print(pkid)
            pj.group_members.add(User.objects.get(id=pkid))
        pj.group_members.add(request.user)
        messages.success(request, f"Project created - {name}")
        return redirect('acc-page')
            
    data = {
        'form' : form,
        'users' : User.objects.all()
    }
    return render(request, 'Intendance/project_CRUD.html', data)


@login_required(login_url='login')
def project_tasks_page(request, pk):
    data = {
        'task_data' : Task.objects.filter(project=pk),
        'project_data' : Project.objects.get(project_id=pk),
    }
    return render(request, 'Intendance/project_tasks.html', data)


@login_required(login_url='login')
def create_task_page(request, project_id):
    form = TaskFormCRUD()
    print("---------------> ",project_id)
    if request.method == "POST":
        print("Create Task -------------: ")
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_status = request.POST.get('task_status')
        print(f"Title ---> {title}")
        print(f"Description ---> {description}")
        print(f"Task Status ---> {task_status}")
        project = Project.objects.get(project_id=project_id)
        task = Task.objects.create(
            project=project,
            title=title,
            description=description,
            task_status=task_status,
            created_by=request.user,
        )
        messages.success(request, f"Task created - {title}")
        return redirect("project-tasks", pk=project.project_id)
        
    data = {
        'form':form,
    }
    return render(request, "Intendance/task_CRUD.html" ,data)

@login_required(login_url='login')
def update_task_page(request, task_id):
    task = Task.objects.get(task_id=task_id)
    form = TaskFormCRUD(instance=task)
    if request.method == "POST":
        form = TaskFormCRUD(request.POST, instance=task)
        title = request.POST.get('title')
        description = request.POST.get('description')
        task_status = request.POST.get('task_status')
        Task.objects.filter(task_id=task_id).update(title=title, description=description, task_status=task_status)
        messages.success(request, f"Task updated")
        return redirect('project-tasks', pk=task.project.project_id)

    data = {
        'form':form,
    }
    return render(request, "Intendance/task_CRUD.html", data)

@login_required(login_url='login')
def delete_task_page(request, task_id):
    task = Task.objects.get(task_id=task_id)
    if request.method == "POST":
        task.delete()
        messages.success(request, f"Task Deleted - {task.title}")
        return redirect('project-tasks', pk=task.project.project_id)
    data = {
        'task':task,
    }
    return render(request, "Intendance/task_removal_confirmation.html", data)