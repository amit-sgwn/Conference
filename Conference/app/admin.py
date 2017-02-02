from django.contrib import admin

from app.models import *

class TrackAdmin(admin.ModelAdmin):
    list_display=('title','description',)
admin.site.register(Track,TrackAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('title','track',)
    search_fields = ['title','abstract']

admin.site.register(Session,SessionAdmin)

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name','bio',)
admin.site.register(Speaker,SpeakerAdmin)
