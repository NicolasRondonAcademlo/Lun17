from email.mime import base
from .views import UserViewSet, UserModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
router.register(r'users',  UserModelViewSet, basename='user')
urlpatterns = router.urls