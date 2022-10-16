import imp
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Intendance.models import Project
from .serializers import ProjectSerializer
from django.contrib.auth.decorators import login_required


@api_view(['GET'])
def get_projects(request):
    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

