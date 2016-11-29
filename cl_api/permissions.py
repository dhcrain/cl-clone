from rest_framework import permissions


# http://www.django-rest-framework.org/api-guide/serializers/#additional-keyword-arguments
class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `user`.
        return obj.user == request.user


# https://github.com/tomchristie/django-rest-framework/blob/master/rest_framework/permissions.py
class IsSuperUserOrReadOnly(permissions.BasePermission):
    """
    Allows access only to superusers users.
    """
    def has_permission(self, request, view):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user and request.user.is_superuser
