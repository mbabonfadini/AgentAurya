from rest_framework.permissions import BasePermission
from tenancy.models import UserTenantModel

class RequiredRoles(BasePermission):
    """
    Permission class to check if the user has the required roles for the current tenant.
    """

    required_roles = ()

    @classmethod
    def as_any(cls, *role_slugs):
        """
        Class method to create a permission class that allows any of the specified roles.
        """
        class _RequiredRoles(cls):
            required_roles = tuple(role_slugs)

        return _RequiredRoles
    

    def has_permission(self, request, view):
        tenant = getattr(request, 'tenant', None)
        user = getattr(request, 'user', None)
        if not tenant or not user or not user.is_authenticated:
            return False
        
        return UserTenantModel.objects.filter(
            user=user, tenant=tenant, is_active=True, role__slug__in=self.required_roles
        ).exists()