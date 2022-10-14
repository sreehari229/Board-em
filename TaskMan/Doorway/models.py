from django.db import models
from django.contrib.auth.models import User


class UserEmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=300)
    email_is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Verfication'
    

class UserForgotPassword(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username