from rest_framework.viewsets import ModelViewSet
from . serializers import ProjectFormSerializer
from . models import ProjectForm


class ProjectFormAPI(ModelViewSet):
    queryset = ProjectForm.objects.all()
    serializer_class = ProjectFormSerializer
