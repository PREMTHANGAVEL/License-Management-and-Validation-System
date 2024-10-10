from rest_framework import serializers
from .models import License

class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = ['key', 'product_name', 'client_name', 'is_active', 'issue_date', 'expiry_date']
