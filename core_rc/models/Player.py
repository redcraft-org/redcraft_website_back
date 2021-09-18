from django.db import models
import uuid


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.CharField(max_length=256, default=None, blank=True, null=True)

    main_language = models.CharField(max_length=32)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"<Player: {self.last_name_minecraft} - {self.last_name_discord}>"

