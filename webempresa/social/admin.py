from django.contrib import admin
from .models import Link
# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created_ad', 'updated_ad')
    
admin.site.register(Link, LinkAdmin)