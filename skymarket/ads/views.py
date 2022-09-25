from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from skymarket.ads.filters import AdFilter
from skymarket.ads.models import Ad, Comment
from skymarket.ads.permissions import UserPermission
from skymarket.ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    permission_classes = (UserPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        if self.action in ["retrieve"]:
            permission_classes = (UserPermission,)
        elif self.action in ["create", "update", "partial_update", "destroy", "me"]:
            permission_classes = (UserPermission,)
        return tuple(permission() for permission in permission_classes)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()

    @action(
        detail=False,
        methods=[
            "get",
        ],
    )
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        user = self.request.user
        serializer.save(author=user, ad=ad_instance)

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_pk")
        ad_instance = get_object_or_404(Ad, id=ad_id)
        return ad_instance.comments.all()

    def get_permissions(self):
        permission_classes = (IsAuthenticated,)
        if self.action in ["list", "retrieve"]:
            permission_classes = (UserPermission,)
        elif self.action in ["create", "update", "partial_update", "destroy"]:
            permission_classes = (UserPermission,)
        return tuple(permission() for permission in permission_classes)

