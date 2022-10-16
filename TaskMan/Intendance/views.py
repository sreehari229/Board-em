from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
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
    return render(request, 'Intendance/project_create.html', data)


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


@login_required(login_url='login')
def change_password(request):
    if request.method == "POST":
        entered_password = request.POST.get('currentPassword')
        if check_password(entered_password, request.user.password):
            new_password = request.POST.get('inputPasswordNew')
            new_password_verify = request.POST.get('inputPasswordNewVerify')
            if new_password == new_password_verify:
                user_obj = User.objects.get(username=request.user.username)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request, "Password changed!")
                return redirect('profile')
            else:
                messages.warning(request, "New Password does not match! Please re-enter password")
                return redirect('change-password')
        else:
            messages.warning(request, "Your current password does not match with existing password.")
            return redirect('change-password')
    
    data = {
        
    }
    return render(request, "Intendance/password_change.html", data)


@login_required(login_url='login')
def delete_project_page(request, project_id):
    project_obj = Project.objects.get(project_id=project_id)
    if request.method == "POST":
        confirmation_text = request.POST.get('Iagreeinp')
        if confirmation_text == "I agree to delete project":
            project_obj.delete()
            messages.success(request, "Project Deleted!")
            return redirect('acc-page')
        else:
            messages.warning(request, "Please type the below statement to confirm the deletion of Project!")
            return redirect('delete-project')
    data = {
        'project':project_obj,
    }
    return render(request, "Intendance/delete_project.html", data)


@login_required(login_url='login')
def search_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        profiles = User.objects.filter(username__icontains=username)
        data = {
            'profiles':profiles,
        }
        return render(request, "Intendance/search_user.html", data)
    else:
        return redirect("acc-page")
    

@login_required(login_url='login')
def searched_profile(request, username):
    userobj = User.objects.get(username=username)
    data = {
        'userobj':userobj,
    }
    return render(request, "Intendance/searched_profile.html", data)


@login_required(login_url='login')
def update_project_settings(request, project_id):
    project_obj = Project.objects.get(project_id=project_id)
    project_form = UpdateProjectForm(instance=project_obj)
    data = {
        'project':project_obj,
        'form':project_form,
    }
    
    if request.method == "POST":
        form = UpdateProjectForm(request.POST, instance=project_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Project settings updated.")
            return redirect('project-tasks', pk=project_id)
    
    return render(request, "Intendance/project_update.html", data)


@login_required(login_url='login')
def leave_project(request, project_id):
    project_obj = Project.objects.get(project_id=project_id)
    if request.method == "POST":
        confirmation_text = request.POST.get('Iagreeinp')
        if confirmation_text == "Leave project":
            project_obj.group_members.remove(request.user)
            messages.success(request, f"Removed from Project {project_obj.name}")
            return redirect("acc-page")
    data = {
        'project':project_obj,
    }
    return render(request, "Intendance/leave_project.html", data)


@login_required(login_url='login')
def compose_group_email(request, project_id):
    project_obj = Project.objects.get(project_id=project_id)
    
    data = {
        'project_data':project_obj,
    }
    
    if request.method == "POST":
        subject = "Board 'em " + request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [member.email for member in project_obj.group_members.all()]
        print(recipient_list)
        try:
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject, message, email_from, recipient_list)
            messages.success(request, "Email sent successfully.")
            return redirect('project-tasks', pk=project_id)
        except Exception as e:
            messages.success(request, "Error has occured, Email Not sent.")
            return redirect('project-tasks', pk=project_id)
    return render(request, "Intendance/group_email_compose.html", data)