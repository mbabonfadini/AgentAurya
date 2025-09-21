from rest_framework.permissions import BasePermission
from tenancy.models import UserTenantModel


class IsTenantUser(BasePermission):
    """
    Permission class to check if the user is associated with the current tenant.
    """
    message = 'User is not associated with the current tenant.'

    def has_permission(self, request, view):
        tenant = getattr(request, 'tenant', None)
        user = getattr(request, 'user', None)

        if not tenant or not user or not user.is_authenticated:
            return False

        return UserTenantModel.objects.filter(
            user=user,
            tenant=tenant,
            is_active=True
        ).exists()