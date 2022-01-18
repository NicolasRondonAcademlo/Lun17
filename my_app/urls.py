from email.mime import base
from .views import UserViewSet, UserModelViewSet, ReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register(r'users', UserViewSet, basename='user')
router.register(r'users',  UserModelViewSet, basename='user')
router.register(r'users_read',  ReadOnlyModelViewSet, basename='user_read')
urlpatterns = router.urls