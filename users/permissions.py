from rest_framework import permissions


class IsModer(permissions.BasePermission):
    message = 'Вы не являетесь модератором.'

    def has_permission(self, request, view):
        return request.user.groups.filter(name='moders').exists()


class IsOwner(permissions.BasePermission):
    message = 'Вы не являетесь владельцем данного объекта.'

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsUserOwner(permissions.BasePermission):
    message = 'Вы можете редактировать только свой профиль.'

    def has_object_permission(self, request, view, obj):
        return obj == request.user
