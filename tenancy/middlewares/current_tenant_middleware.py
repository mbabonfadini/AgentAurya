from django.utils.deprecation import MiddlewareMixin
from tenancy.models import TenantModel


class CurrentTenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        host = request.get_host().split(":")[0]  # remove porta
        parts = host.split(".")

        # Exige pelo menos: [slug].auryabox.com
        if len(parts) < 3:
            request.tenant = None
            return

        slug = parts[0]  # pega o subdomínio (cliente1, cliente2, etc.)
        try:
            tenant = TenantModel.objects.get(slug=slug, is_active=True)
            request.tenant = tenant
        except TenantModel.DoesNotExist:
            request.tenant = None
