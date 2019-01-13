from rest_framework import generics,mixins,permissions
from rest_framework import permissions
from rest_framework.views import APIView
from django.db.models import Q
from rest_framework.response import Response 
from django.contrib.auth import authenticate,get_user_model
from rest_framework_jwt.settings import api_settings
# from .serializers import UserRegisterSerializer
from status.models import Status
from .serializers import UserDetailSerializer
from status.api.serializers import StatusInlineUserSerializer
from accounts.api.utils import jwt_response_payload_handler
from accounts.api.permissions import AnonPermissionOnly

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER

User = get_user_model()
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

class UserStatusAPIView(generics.ListAPIView):
    # queryset = User.objects.filter(is_active=True)
    serializer_class = UserDetailSerializer
    # lookup_field = 'username'

    def get_queryset(self,*args,**kwargs):
        username = self.kwargs.get('username',None)
        if username is None:
            return Status.objects.none()
        return Status.objects.filter(user__username=username)
    