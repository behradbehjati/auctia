from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Item
class ItemAdmin(admin.ModelAdmin):
    ordering=['-create_date']
    list_display=['seller','name']
admin.site.register(Item,ItemAdmin)

class ItemInline(admin.TabularInline):
    model = Item
    fk_name = "seller"
    fields = ('name', 'description')
    extra=0
class CustomUserAdmin(UserAdmin):
    inlines = [ItemInline]

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)