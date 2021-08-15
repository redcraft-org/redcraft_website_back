from django.db import models


class Player(models.Model):
    email = models.CharField(max_length=256)

    language = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Player: {self.last_name_minecraft} - {self.last_name_discord}>"
