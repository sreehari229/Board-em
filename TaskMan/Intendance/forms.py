from tkinter import Widget
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        widgets = {
            'first_name' : forms.TextInput(attrs={
                 'class': "trial_class_css",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name',
                }),
            'last_name' : forms.TextInput(attrs={
                 'class': "trial_class_css",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name',
                }),
        }
        

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'company', 'city', 'website_link', 'github_link', 'image', 'date_of_birth']