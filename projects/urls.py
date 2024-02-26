from rest_framework import routers
from .api import Viewset

router = routers.DefaultRouter()

router.register('project/register', Viewset, 'Projects')

urlpatterns = router.urls