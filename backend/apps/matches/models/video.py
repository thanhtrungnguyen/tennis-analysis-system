from django.db import models
from .match import Match

class Video(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    file = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Video for {self.match} uploaded on {self.uploaded_at}"