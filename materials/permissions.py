from rest_framework.permissions import BasePermission


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return request.user == view.get_object().owner

class IsManager(BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='manager').exists():
            return True

class IsOwner(BasePermission):

    def has_permission(self, request, view):
        if request.user == view.get_object().owner:
            return True