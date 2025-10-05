from django.contrib import admin
from django.utils.html import format_html
from .models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'short_description_trunc', 'open_link')
    list_display_links = ('title',)
    search_fields = ('title', 'short_description')
    ordering = ('order', '-created_at')
    list_per_page = 25

    fieldsets = (
        ('Job Details', {
            'fields': ('title', 'image', 'short_description', 'order'),
        }),
        ('Link', {
            'fields': ('external_link',),
        }),
        ('Metadata', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if 'image' in form.base_fields:
            form.base_fields['image'].label = 'Upload Job Image'
        if 'external_link' in form.base_fields:
            form.base_fields['external_link'].label = 'External Link (optional)'
        return form

    def short_description_trunc(self, obj):
        if not obj.short_description:
            return '-'
        return (obj.short_description[:60] + '...') if len(obj.short_description) > 60 else obj.short_description
    short_description_trunc.short_description = 'Description'

    def open_link(self, obj):
        url = obj.external_link or (obj.get_absolute_url() if hasattr(obj, 'get_absolute_url') else None)
        if not url:
            return '-'
        label = 'Open' if obj.external_link else 'View'
        return format_html('<a href="{}" target="_blank" rel="noopener">{}</a>', url, label)
    open_link.short_description = 'Open'
