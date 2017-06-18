from django.db import models

from cosplay_codex.users.models import User


class Costume(models.Model):
    """Represents a costume."""
    name = models.CharField(max_length=100)
    series = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name
