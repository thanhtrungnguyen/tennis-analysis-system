from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Player, Match, MatchPlayer, Video, Event, VideoSegment

admin.site.register(Player)
admin.site.register(Match)
admin.site.register(MatchPlayer)
admin.site.register(Video)
admin.site.register(Event)
admin.site.register(VideoSegment)
