from django.contrib import admin
from django.utils.html import format_html

from .models import Blank, Employee


@admin.register(Blank)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'employee', "latitude", 'longitude', 'view_image', 'status', 'comment')
    search_fields = ('id',)
    list_filter = ('status', 'employee')
    readonly_fields = ('view_image',)

    def view_image(self, obj):
        return format_html('<img src="{}" height="60" />'.format(obj.photo.url)) if obj.photo else '-'


@admin.register(Employee)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'mfo', "tab_number", 'crm_id', 'telegram_id', 'status')
    search_fields = ('id', 'mfo', 'tab_number', 'crm_id', 'telegram_id')
    list_filter = ('status',)
