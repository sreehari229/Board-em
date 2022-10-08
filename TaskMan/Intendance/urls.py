from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_index_page, name='acc-page'),
    path('profile/', views.profile_page, name='profile'),
    path('create_project/', views.create_project_page, name='create-project'),
    path('project_task/<str:pk>/', views.project_tasks_page, name='project-tasks'),
    path('create_task/<str:project_id>/', views.create_task_page, name='create-task'),
    path('update_task/<str:task_id>/', views.update_task_page, name="update-task"),
    path('delete_task/<str:task_id>/', views.delete_task_page, name="delete-task"),
]

