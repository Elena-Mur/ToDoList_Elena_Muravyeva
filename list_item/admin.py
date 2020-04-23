from django.contrib import admin
from list_item.models import Listitem


# Register your models here.
class ListitemAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'name', 'is_done', 'list', 'priority']
    list_filter = ['created', 'name', 'is_done', 'list']
    search_fields = ['name', 'list']


admin.site.register(Listitem, ListitemAdmin)
