from email.mime import base
from .views import UserViewSet, UserModelViewSet, ReadOnlyModelViewSet, UserReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

# router.register(r'users', UserViewSet, basename='user')
router.register(r'users',  UserModelViewSet, basename='user')
router.register(r'users_read',  UserReadOnlyModelViewSet, basename='user_read')
urlpatterns = router.urls 