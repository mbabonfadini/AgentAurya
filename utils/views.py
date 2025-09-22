from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from drf_spectacular.views import SpectacularSwaggerView


@method_decorator(staff_member_required, name='dispatch')
class ProtectedSwaggerView(SpectacularSwaggerView):
    """Swagger view protected to staff members only."""
    pass
