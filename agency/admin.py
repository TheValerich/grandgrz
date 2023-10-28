from django.contrib import admin
from .models import Estate, Category, EstateImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


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
    prepopulated_fields = {'slug': ('name',)}
    inlines = [EstateImageInline, ]


admin.site.register(EstateImage, EstateImageAdmin)
admin.site.register(Estate, EstateAdmin)
