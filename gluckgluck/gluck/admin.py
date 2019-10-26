from django.contrib import admin
from .models import Event, Page, Component, Section

# Register your models here.

class ComponentInline(admin.TabularInline):
    model = Component
    min_num = 1
    can_delete = True
    extra = 0


class SectionInline(admin.TabularInline):
    model = Section
    min_num = 1
    can_delete = True
    extra = 0


class PageAdmin(admin.ModelAdmin):
    inlines = [
        SectionInline,
        ComponentInline,
    ]

class SectionAdmin(admin.ModelAdmin):
    inlines = [
        ComponentInline,
    ]


class EventAdmin(admin.ModelAdmin):
    exclude = ('active', 'published_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Component)

