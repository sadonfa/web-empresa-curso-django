from django.contrib import admin
from .models import Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_ad', 'updated_ad')
    
admin.site.register(Page, PageAdmin)