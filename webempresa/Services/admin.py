from django.contrib import admin
from .models import Service

# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created_ad', 'updated_ad')
    list_display = ('title', 'subtitle', 'image', 'created_ad', 'updated_ad')

admin.site.register(Service, ServiceAdmin)