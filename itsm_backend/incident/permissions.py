from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'employee'


class IsSupport(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'support'
