import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Intendance.models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def endpoints(request):
    data = {
        'Get Logged in user':"localhost:8000/api/get-user/",
        'Get Project Details' : "localhost:8000/api/get-project-details/<project_id>/",
        'Get all tasks under a project' : "localhost:8000/api/get-tasks/<project_id>/",
    }
    return Response(data)

@api_view(['GET'])
def get_logged_in_user(request):
    if request.user.is_authenticated:
        data = {
            'username':request.user.username,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
            'user_id' : request.user.id
        }
    else:
        data = {
            'result' : "user not logged in"
        }
    return Response(data)

@api_view(['GET'])
def get_project_details(request,project_id):
    project_obj = Project.objects.get(project_id=project_id)
    serializer = ProjectSerializer(project_obj, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def get_tasks(request, project_id):
    project_obj = Project.objects.get(project_id=project_id)
    tasks_obj = Task.objects.filter(project=project_obj)
    serializer = TaskSerializer(tasks_obj, many=True)
    return Response(serializer.data)