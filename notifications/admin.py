from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'url', 'created_at')
    ordering = ('order',)
    search_fields = ('title', 'url')

    fieldsets = (
        ('Notification Info', {
            'fields': ('title', 'url', 'order'),
        }),
    )
