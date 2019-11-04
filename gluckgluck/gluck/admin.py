from django.contrib import admin
from merged_inlines.admin import MergedInlineAdmin
from .models import Event, Section, Page, Text, Image
from django.contrib.auth.models import User, Group

# Register your models here.



class SectionInline(admin.TabularInline):
    model = Section
    can_delete = True
    extra = 0
    min_num = 0
    fields = ['section_title', 'text', 'image', 'image_tag']
    readonly_fields = ['image_tag']

class TextInline(admin.TabularInline):
    model = Text
    extra = 0
    min_num = 0
    fields = ['order', 'text']


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    min_num = 0
    fields = ['order', 'image', 'image_tag']
    readonly_fields = ['image_tag']

class PageAdmin(MergedInlineAdmin):
    model = Page
    inlines = [
        TextInline,ImageInline
    ]
    merged_inline_order = 'order'

class EventAdmin(admin.ModelAdmin):
    exclude = ('active', 'published_date')


admin.site.register(Event, EventAdmin)
admin.site.register(Page, PageAdmin)
admin.site.site_header = "GluckGluck Admin"
admin.site.site_title = ""
admin.site.index_title = ""
admin.site.unregister(Group)