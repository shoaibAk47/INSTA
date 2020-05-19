from django.contrib import admin
from .models import Entity
# Register your models here.

class EntityAdmin(admin.ModelAdmin):
    model=Entity
    list_display = ('get_name','image', 'created_at','updated_at','id')
    list_filter = ('created_at','updated_at')
    search_fields = ['id']
    def get_name(self,obj):
        return obj.user.username

    get_name.short_description = 'User Name'

admin.site.register(Entity,EntityAdmin)