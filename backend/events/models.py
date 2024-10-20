from django.db import models

from matches.models import Match
from players.models import Player
from videos.models import Video


class Event(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50)
    player = models.ForeignKey(Player, null=True, blank=True, on_delete=models.SET_NULL)
    event_time = models.DateTimeField()


class VideoSegment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
