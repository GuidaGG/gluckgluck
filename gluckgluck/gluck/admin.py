from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    exclude = ('active', 'published_date')

admin.site.register(Event, EventAdmin)

# Register your models here.

