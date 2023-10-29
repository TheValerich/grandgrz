from django.contrib import admin
from .models import Estate, Category, EstateImage, Workers, Requisites


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class EstateImageAdmin(admin.ModelAdmin):
    list_display = ['estate', 'image']
    list_filter = ['estate']
    list_editable = ['image']


class EstateImageInline(admin.StackedInline):
    model = EstateImage
    extra = 0
    max_num = 10


class EstateAdmin(admin.ModelAdmin):
    list_display = ['name', 'rooms', 'area', 'available', 'best_offer']
    list_filter = ['category', 'name', 'rooms', 'area', 'material', 'available', 'best_offer']
    list_editable = ['rooms', 'area', 'available', 'best_offer']
    inlines = [EstateImageInline, ]


@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Requisites)
class RequisitesAdmin(admin.ModelAdmin):
    list_display = ['bank']


admin.site.register(EstateImage, EstateImageAdmin)
admin.site.register(Estate, EstateAdmin)
