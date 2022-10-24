from email.policy import default
from enum import unique
from django.db import models
from django.contrib.auth.models import User
from PIL import Image as pilimg
import uuid
import datetime

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    website_link = models.URLField(max_length=500, null=True, blank=True)
    github_link = models.URLField(max_length=500, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    date_of_birth = models.DateField(null=True, blank=True)
    account_creation_date = models.DateField(auto_now_add=True)
    account_modified_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} - {self.user.username}'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save()
        img = pilimg.open(self.image.path)
        if img.height > 500 or img.width > 500:
            output_size = (500,500)
            img.thumbnail(output_size)
            img.save(self.image.path)
            


class Project(models.Model):
    project_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    group_members = models.ManyToManyField(User, blank=True, related_name="group_members")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
    created_date = models.DateField(auto_now_add=True)
    start_date = models.DateField()
    duration = models.PositiveIntegerField()
    modified_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'{self.project_id} - {self.name}'
    

class Task(models.Model):
    status_choice = (
        ('todo', 'ToDo'),
        ('inprogress', 'In-Progress'),
        ('testing', 'Testing'),
        ('completed', 'Completed'),
    )
    task_id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)    
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    task_status = models.CharField(max_length=100, choices=status_choice, default='todo')
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.title}'


class Project_Invitation(models.Model):
    invite_status = (
        ('sent', 'Sent'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, choices=invite_status, default='sent')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('project', 'receiver',)
    
    def __str__(self):
        return f"{self.receiver} invited for {self.project}"
    

class NotificationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.user} - {self.title}"
    

class Reasons(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.user} - {self.project}"

class Discussions(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    message = models.TextField()
    posted_on = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.posted_by} - {self.project}"
    