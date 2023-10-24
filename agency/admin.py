from django.contrib import admin
from .models import Estate, Category


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    list_display = ['name', 'rooms', 'area', 'available', 'best_offer']
    list_filter = ['name', 'rooms', 'area', 'material', 'available', 'best_offer']
    list_editable = ['rooms', 'area', 'available', 'best_offer']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
