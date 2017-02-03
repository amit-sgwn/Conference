from django.contrib import admin

from app.models import *

class TrackAdmin(admin.ModelAdmin):
    list_display=('title','description',)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('title','status',)
    search_fields = ['title','abstract']
    list_filter = ('track','speaker',)
    actions = ['make_approved',]

    def make_approved(self,request,queryset):
        row_updated = queryset.update(status = 'a')
        if row_updated == 1:
            message_bit = "1 session was "
        else:
            message_bit = "%s session were "%row_updated

        self.message_user(request,"%s approved"%message_bit)
        
    make_approved.short_description = "Mark session(s) as approved"


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name','bio',)
    fieldsets  = (
        ("General Information ",{"fields": ("name","bio",)}),
         ("Social Media",{
             "classes":("collapse"),
             "fields":("twitter","facebook"),
             "description":"Add social media here"})
        )



admin.site.register(Speaker,SpeakerAdmin)
admin.site.register(Track,TrackAdmin)
admin.site.register(Session,SessionAdmin)
