from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoints),
    path('get-user/', views.get_logged_in_user),
    path('get-project-details/<str:project_id>/', views.get_project_details),
    path('get-tasks/<str:project_id>/', views.get_tasks),
    path('create-task/', views.create_task),
]