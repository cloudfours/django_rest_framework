from rest_framework import routers
from .api import ProjectviewsSet
router=routers.DefaultRouter()

router.register('api/projects',ProjectviewsSet,'projects')

urlpatterns=router.urls