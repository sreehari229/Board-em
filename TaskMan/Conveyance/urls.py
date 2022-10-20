from django.urls import path
from . import views

urlpatterns = [
    path('get-user/', views.get_logged_in_user, name='api-user'),
    path('get-project/', views.get_logged_in_user, name='api-user'),
]