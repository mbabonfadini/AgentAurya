from django.utils.deprecation import MiddlewareMixin
from tenancy.models import TenantModel
from django.conf import settings

class CurrentTenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # pega o path e quebra em partes
        path_parts = [p for p in request.path.split("/") if p]

        if not path_parts:
            request.tenant = None
            return

        slug = path_parts[0]  # primeira parte da URL após o domínio

        try:
            tenant = TenantModel.objects.get(slug=slug, is_active=True)
            request.tenant = tenant
            # opcional: sobrescreve o path para que as views não precisem lidar com o slug
            request.path_info = "/" + "/".join(path_parts[1:])
        except TenantModel.DoesNotExist:
            if settings.DEBUG:
                request.tenant = TenantModel.objects.first()
            else:
                request.tenant = None
