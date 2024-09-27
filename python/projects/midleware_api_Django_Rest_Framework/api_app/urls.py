
from rest_framework.routers import DefaultRouter
from .views import MessageViewSet

router = DefaultRouter()
router.register(r'messages', MessageViewSet)

urlpatterns = router.urls


# api_app/urls.py
#from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
#router.register(r'tasks', TaskModelViewSet, basename='task')

urlpatterns = router.urls



