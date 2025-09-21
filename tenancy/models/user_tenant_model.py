from django.db import models
from django.conf import settings
from tenancy.models import TenantModel, RolesModel


class UserTenantModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    tenant = models.ForeignKey(TenantModel, on_delete=models.CASCADE)
    role = models.ForeignKey(RolesModel, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_user_tenants'
        unique_together = ('user', 'tenant')
        indexes = (
            models.Index(fields=['tenant', 'role']),
        )
        verbose_name = 'User Tenant'
        verbose_name_plural = 'User Tenants'
    