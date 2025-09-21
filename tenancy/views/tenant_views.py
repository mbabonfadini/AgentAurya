from rest_framework import generics, status
from tenancy.models import TenantModel
from tenancy.serializers import TenantCreateSerializer


class TenantCreateView(generics.CreateAPIView):
    queryset = TenantModel.objects.all()
    serializer_class = TenantCreateSerializer