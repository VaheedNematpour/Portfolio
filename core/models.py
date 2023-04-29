from django.db import models


class Portfolio(models.Model):
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256)
    birth_date = models.DateField(blank=True, null=True)
    bio = models.TextField()
    image = models.ImageField(
        upload_to='portfolio/image', blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['first_name', 'last_name']


class Skill(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    level = models.CharField(max_length=256)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='skill')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    portfolio = models.ForeignKey(
        Portfolio, on_delete=models.CASCADE, related_name='project')

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['title']


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='project/image')
