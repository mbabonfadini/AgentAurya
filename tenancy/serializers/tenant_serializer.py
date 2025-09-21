from django.contrib.auth import get_user_model
from django.utils.text import slugify
from rest_framework import serializers
from tenancy.models import UserTenantModel, TenantModel, RolesModel

User = get_user_model()


class TenantCreateSerializer(serializers.ModelSerializer):
    # First data
    user_email = serializers.EmailField(write_only=True)
    user_password = serializers.CharField(write_only=True, min_length=8)
    user_name = serializers.CharField(write_only=True, max_length=255)

    class Meta:
        model = TenantModel
        fields = ["id", "name", "slug", "is_active", "user_email", "user_password", "user_name"]
        read_only_fields = ['id', 'is_active', 'slug']

    def create(self, validated_data):
        user_email = validated_data.pop('user_email')
        user_password = validated_data.pop('user_password')
        user_name = validated_data.pop('user_name')
        name = validated_data.get('name')

        slug = slugify(name)

        tenant = TenantModel.objects.create(
            name=name, slug=slug, **validated_data)

        user = User.objects.create_user(
            email=user_email,
            password=user_password,
            first_name=user_name
        )

        role, _ = RolesModel.objects.get_or_create(
            slug="owner",
            defaults={"name": "Owner", "description": "Tenant owner"}
        )

        UserTenantModel.objects.create(
            user=user, tenant=tenant, role=role, is_active=True)

        return tenant
