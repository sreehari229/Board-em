from django.db import models
from django.contrib.auth.models import User


class UserEmailVerification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_token = models.CharField(max_length=300)
    email_is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.username} Verfication'