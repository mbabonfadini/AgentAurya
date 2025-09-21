from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tenancy.models import UserTenantModel


class SessionLoginView(APIView):
    """
    POST {"e-mail": "...", "password":"..."}
    Rejects if the user is not associated with the current tenant.
    """

    authentication_classes = []
    permission_classes = []


    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        tenant = getattr(request, 'tenant', None)
        
        if not tenant:
            return Response({'detail': 'Tenant not found in request.'}, status=status.HTTP_400_BAD_REQUEST)
        

        user = authenticate(request, email=email, password=password)
        
        if not user:
            return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        linked = UserTenantModel.objects.filter(
            user=user, tenant=tenant, is_active=True
        ).exists()

        if not linked:
            return Response({'detail': 'User is not associated with the current tenant.'}, status=status.HTTP_403_FORBIDDEN)
        
        login(request, user)  # sessão
        return Response({"detail": "ok"})