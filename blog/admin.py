from django.contrib import admin
from .models import Category, Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_ad', 'updated_ad')
    list_display = ('name', 'created_ad', 'updated_ad')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_ad', 'updated_ad')
    list_display = ('title', 'autorh', 'published')
    search_fields = ('title', 'autorh')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)