import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Intendance.models import Project
from .serializers import ProjectSerializer
from django.contrib.auth.decorators import login_required


# @api_view(['GET'])
# def get_projects(request):
#     projects = Project.objects.all()
#     serializer = ProjectSerializer(projects, many=True)
#     return Response({
#         'username':request.user.username,
#     })

@api_view(['GET'])
def get_logged_in_user(request):
    data = {
        'username':request.user.username,
        'first_name' : request.user.first_name,
        'last_name' : request.user.last_name,
        'email' : request.user.email,
        'user_id' : request.user.id
    }
    return Response(data)