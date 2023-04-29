from rest_framework_nested import routers
from . import views


router = routers.DefaultRouter()
router.register('project', views.ProjectViewSet, basename='projects')
router.register('skill', views.SkillViewSet, basename='skills')


urlpatterns = router.urls
