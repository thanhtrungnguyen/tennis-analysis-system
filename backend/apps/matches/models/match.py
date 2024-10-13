from django.db import models
from .player import Player

class Match(models.Model):
    tournament_name = models.CharField(max_length=100)
    match_date = models.DateField()
    match_type = models.CharField(max_length=10, choices=[('Singles', 'Singles'), ('Doubles', 'Doubles')])
    result = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tournament_name} on {self.match_date}"

class MatchPlayer(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    role = models.CharField(max_length=20)