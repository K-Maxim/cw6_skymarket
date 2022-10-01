# TODO здесь производится настройка пермишенов для нашего проекта
from rest_framework.permissions import BasePermission
from users.models import User


class UserPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN:
            return True

        if view.action == 'retrieve':
            return True

        if view.action in ["create", "update", "partial_update", "destroy"]:
            return obj.author == request.user or request.user.role == User.ADMIN

