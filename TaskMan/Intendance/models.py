from email.policy import default
import imp
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.SlugField(max_length=500, null=True, blank=True)
    github_link = models.SlugField(max_length=500, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    account_creation_date = models.DateField(auto_now_add=True)
    account_modified_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'