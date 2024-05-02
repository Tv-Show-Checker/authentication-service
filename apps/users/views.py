import requests
from django.contrib.auth import get_user_model
from django_redis import get_redis_connection
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from apps.users.permissions import UserPermission
from apps.users.serializers import UserSerializer
from django.core.cache import cache


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    # @action(methods=['post'], detail=False, url_path='test')
    # def test(self, request, *args, **kwargs):
    #     response = requests.post('http://advance-app.local:8002/api/user/profiles/test/', data={
    #         "url": request.data.get('url')
    #     })
    #     print(response)
        # return Response({"message": "send from auth"}, status=status.HTTP_200_OK)
