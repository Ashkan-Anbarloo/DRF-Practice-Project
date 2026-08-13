from rest_framework import permissions
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