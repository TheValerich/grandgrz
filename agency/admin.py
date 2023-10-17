from django.contrib import admin
from .models import Estate, Category


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['rooms', 'area', 'available']
    list_display_links = None
    list_filter = ['rooms', 'area', 'material', 'available']
    list_editable = ['rooms', 'available']
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
