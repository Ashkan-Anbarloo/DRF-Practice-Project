from rest_framework import permissions
from rest_framework.permissions import SAFE_METHODS
from .models import BlockUserModel


class BlocklistPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        # blocked = BlockUserModel.objects.filter(user=user).exists()
        # return not blocked
        if not user.is_authenticated:
            return False
        if BlockUserModel.objects.filter(user=user).exists():
            return False
        return True
    

class BookPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if BlockUserModel.objects.filter(user=request.user).exists():
            return False
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user