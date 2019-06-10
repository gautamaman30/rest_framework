from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    """
    permissions to allow only owners to update,delete or edit snippet
    """

    def has_object_permission(self, request, view, obj):
        """
        safe methods include get,head etc
        """
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user

