from django.contrib import admin
from tenancy.models import TenantModel, UserTenantModel, RolesModel
# Register your models here.
admin.site.register([TenantModel, UserTenantModel, RolesModel])