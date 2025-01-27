from .base import BaseModelViewset
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from django.db.models import Q

from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from ..serializers import (
    UserProfileSerializer,
    UserSerializer,
    PermissionSerializer,
)
from ..permissions import CamomillaSuperUser, CamomillaBasePermissions, ReadOnly


class CamomillaObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})


class UserViewSet(BaseModelViewset):

    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    model = get_user_model()
    permission_classes = (CamomillaSuperUser | CamomillaBasePermissions,)

    @action(detail=False, methods=["get", "put"], permission_classes=(IsAuthenticated,))
    def current(self, request):
        user = request.user
        if request.method == "PUT":
            serialized_user = UserProfileSerializer(
                user, data=request.data, partial=True
            )
            if serialized_user.is_valid(raise_exception=True):
                user = serialized_user.save()
        return Response(UserProfileSerializer(user, context={"request": request}).data)

    @action(detail=True, methods=["post"])
    def kickout(self, request, pk=None):
        user = self.get_object()
        try:
            user.auth_token.delete()
        except Exception:
            pass
        return Response({})


class PermissionViewSet(BaseModelViewset):

    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    model = Permission
    permission_classes = (CamomillaSuperUser | ReadOnly,)
    http_method_names = ["get", "put", "options", "head"]

    def get_queryset(self):
        permissions = Permission.objects.filter(
            Q(content_type__app_label__contains="camomilla")
            | Q(content_type__app_label__contains="plugin_")
            | Q(content_type__model="token")
            | Q(content_type__model="user")
        )
        return permissions
