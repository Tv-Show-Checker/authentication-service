from django.urls import path, include
from rest_framework import routers
from apps.users import views

router = routers.SimpleRouter()
router.register(r'', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]