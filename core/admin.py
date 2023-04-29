from django.contrib import admin
from . import models


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ProjectImageInline]


@admin.register(models.Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title']
