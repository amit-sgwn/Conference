from django.contrib import admin

from app.models import *

class TrackAdmin(admin.ModelAdmin):
    list_display=('title','description',)
admin.site.register(Track,TrackAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('title','track',)
    search_fields = ['title','abstract']
    list_filter = ('track','speaker',)

admin.site.register(Session,SessionAdmin)

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
