from rest_framework.serializers import ModelSerializer
from Intendance.models import Project, Task


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        
class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'