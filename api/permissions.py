from rest_framework import permissions


# checks whether the requesting user is the owner of the given object
class OwnerAuthentication(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user
