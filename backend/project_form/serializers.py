from rest_framework import serializers
from .models import ProjectForm


class ProjectFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectForm
        fields = '__all__'
