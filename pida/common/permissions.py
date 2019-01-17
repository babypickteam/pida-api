from rest_framework import permissions


class IsAuthenticatedOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and \
                    request.user.is_authenticated and \
                    obj.owner == request.user)


class IsAuthenticatedOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and \
                    request.user.is_authenticated and \
                    obj.owner == request.user)
