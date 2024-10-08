from django.urls import path
from .views import ClientViewSet, ProjectViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = router.urls
