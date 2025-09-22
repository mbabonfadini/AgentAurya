from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.utils import extend_schema
from utils.views import ProtectedSwaggerView


class HiddenSchemaView(SpectacularAPIView):
    @extend_schema(exclude=True)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    

urlpatterns = [
    path('admin/', admin.site.urls),
    # interface Swagger
    path("api/", ProtectedSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
     # gera o schema OpenAPI
    path("api/schema/", HiddenSchemaView.as_view(), name="schema"),
    path('auth/', include('core_auth.urls.session_urls')),
]
