from django.db import models


class PlayerLanguage(models.Model):
    player = models.ForeignKey(
        'Player',
        related_name='languages',
        on_delete=models.CASCADE
    )

    language = models.ForeignKey(
        'Language',
        related_name='player_language',
        on_delete=models.CASCADE
    )

    main_language = models.BooleanField()
