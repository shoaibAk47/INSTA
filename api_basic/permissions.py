from rest_framework import permissions
message = 'You must be the owner of this object.'

class IsAuthenticatedAndOwner(permissions.BasePermission):
    message = 'You are not the owner of this article, You must be the owner of this object to access this'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user