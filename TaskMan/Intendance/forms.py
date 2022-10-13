from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Project, Task


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'company', 'city', 'website_link', 'github_link', 'image', 'date_of_birth']

        
class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        

class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name','description','url','group_members','start_date','duration']

        
class TaskFormCRUD(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'