from rest_framework.viewsets import ModelViewSet
from .models import Portfolio, Project, Skill
from . import serializers


class ProjectViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Project.objects.prefetch_related('images').all()
    serializer_class = serializers.ProjectSerializer


class SkillViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Skill.objects.all()
    serializer_class = serializers.SkillSerializer


class PortfolioViewSet(ModelViewSet):
    http_method_names = ['get']
    queryset = Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
