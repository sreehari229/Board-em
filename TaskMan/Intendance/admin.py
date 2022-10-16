from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Project_Invitation)
admin.site.register(NotificationUser)