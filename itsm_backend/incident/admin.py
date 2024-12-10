from django.contrib import admin
from .models import Incident

@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'status', 'team', 'responsible', 'created_at', 'created_by')
    list_filter = ('type', 'status', 'team', 'created_at')
    search_fields = ('topic', 'description', 'team', 'responsible__username', 'created_by__username')
    ordering = ('-created_at',)
