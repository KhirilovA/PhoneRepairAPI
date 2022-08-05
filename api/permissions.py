from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser


class IsLoggedIn(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return not isinstance(request.user, AnonymousUser)


class IsOwnerOrMasterRequest(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff


class IsOwnerOrMasterInvoice(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.request.user == request.user or request.user.is_staff


class IsMaster(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff


class IsOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsOwnerAndNotInProgress(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user and obj.status == 1

class IsMasterOrNotInProgress(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.status == 1


class IsMasterAndNotPaid(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_staff and obj.paid == 1


class IsMasterAndNotPaidOrOwner(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return (request.user.is_staff and obj.paid == 1)\
               or obj.request.user == request.user
