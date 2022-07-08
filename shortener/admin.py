from django.contrib import admin
from .models import UniformResourceLocator
from .models import RedirectClickCount


# Register your models here.
@admin.register(UniformResourceLocator)
class UniformResourceLocatorAdmin(admin.ModelAdmin):
    list_display = ('id','url','alias', 'created_by', 'created_at')
    ordering = ('-created_at',)
    search_fields = ('url', 'alias')
    list_filter = ('created_by', 'created_at')
    readonly_fields = ('created_at', 'edited_at')


@admin.register(RedirectClickCount)
class RedirectClickCountAdmin(admin.ModelAdmin):
    list_display = ('link', 'clicks_count', 'clicked_at', 'ip_address')
    ordering = ('-clicked_at',)
    search_fields = ('link', 'ip_address')
    list_filter = ('clicked_at',)
    readonly_fields = ('clicked_at',)
