from django.contrib import admin
from .models import Estate


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['name', 'rooms', 'area', 'available']
    list_filter = ['name', 'rooms', 'area', 'material', 'available']
    list_editable = ['rooms', 'available']
    prepopulated_fields = {'slug': ('name',)}
