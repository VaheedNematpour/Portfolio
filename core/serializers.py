from rest_framework import serializers
from . import models


class SimpleProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ['title', 'description']


class SimpleSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['title', 'description', 'level']


class PortfolioSerializer(serializers.ModelSerializer):
    project = SimpleProjectSerializer(many=True, read_only=True)
    skill = SimpleSkillSerializer(many=True, read_only=True)

    class Meta:
        model = models.Portfolio
        fields = ['id', 'first_name', 'last_name',
                  'bio', 'birth_date', 'image', 'skill', 'project']


class ProjectImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProjectImage
        fields = ['id', 'image']


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ['id', 'title', 'description', 'images']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ['id', 'title', 'description', 'level']
