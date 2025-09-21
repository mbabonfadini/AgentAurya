from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', admin.site.urls),
    path('auth/', include('core_auth.urls.session_urls')),
]
