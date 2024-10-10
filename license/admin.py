from django.contrib import admin
from .models import License

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'client_name', 'is_active', 'expiry_date')
    search_fields = ('product_name', 'client_name')
    list_filter = ('is_active',)

admin.site.register(License, LicenseAdmin)
