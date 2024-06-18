from django.contrib import admin
from .models import *


admin.site.site_title = admin.site.site_header = 'Priority Soft Inventory Admin'


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active', 'created_on', 'updated_on')
    list_display_links = [i for i in list_display[:2]]
    search_fields = ('name', 'contact_info')
    list_filter = (
        'active',
        'created_on',
        'updated_on',
    )


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'suppliers_count', 'active', 'created_on', 'updated_on')
    list_display_links = [i for i in list_display[:2]]
    search_fields = ('name', 'description')
    filter_horizontal = ('suppliers',)
    list_filter = (
        'active',
        'created_on',
        'updated_on',
    )



