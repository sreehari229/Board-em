from django.urls import path
from . import views

urlpatterns = [
    path('', views.acc_index_page, name='acc-page'),
    path('profile/', views.profile_page, name='profile'),
    path('change_password/', views.change_password, name="change-password"),
    path('project_task/<str:pk>/', views.project_tasks_page, name="project-tasks"),
    path('search_user/', views.search_user, name="search-user"),
    path('searched_profile/<str:username>/', views.searched_profile, name="searched-profile"),
    path('group_email/<str:project_id>/', views.compose_group_email, name="group-email"),
    #Related to Tasks
    path('create_task/<str:project_id>/', views.create_task_page, name='create-task'),
    path('update_task/<str:task_id>/', views.update_task_page, name="update-task"),
    path('delete_task/<str:task_id>/', views.delete_task_page, name="delete-task"),
    #Related to Project
    path('create_project/', views.create_project_page, name='create-project'),
    path('delete_project/<str:project_id>/', views.delete_project_page, name="delete-project"),
    path('update_project_settings/<str:project_id>/', views.update_project_settings, name="update-project"),
    path('leave_project/<str:project_id>/', views.leave_project, name="leave-project"),
    path('discussion_board/<str:project_id>/', views.project_discussion_page, name="discussion-board"),
    path('download_as_csv/<str:project_id>', views.download_as_csv, name="download-data-csv"),
]

