from django.contrib import admin
from merged_inlines.admin import MergedInlineAdmin
from inline_ordering.admin import OrderableStackedInline
from .models import Event, Section, Page


# Register your models here.



class SectionInline(OrderableStackedInline):
    model = Section
    can_delete = True
    extra = 1
    min_num = 1
    
 
class PageAdmin(admin.ModelAdmin):
    model = Page
    inlines = [
        SectionInline
    ]

class EventAdmin(admin.ModelAdmin):
    exclude = ('active', 'published_date')

admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)

