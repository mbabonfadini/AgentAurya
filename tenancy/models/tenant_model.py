from django.db import models


class TenantModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tb_tenants'
        verbose_name = 'Tenant'
        verbose_name_plural = 'Tenants'
    

    def __str__(self):
        return self.name