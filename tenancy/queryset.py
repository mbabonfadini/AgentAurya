from rest_framework.exceptions import PermissionDenied


class TenantScopedQuerySetMixin:
    tenant_field = "tenant"

    def get_queryset(self):
        qs = super().get_queryset()
        tenant = getattr(self.request, "tenant", None)
        if not tenant:
            raise PermissionDenied("Tenant ausente.")
        return qs.filter(**{self.tenant_field: tenant})