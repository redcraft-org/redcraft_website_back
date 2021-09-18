from django.db import models


class PlayerInfoProvider(models.Model):
    TYPE_PROVIDERS = (
        ('mc', 'Minecraft'),
        ('di', 'Discord'),
    )

    player = models.ForeignKey(
        'Player',
        related_name='info',
        on_delete=models.CASCADE
    )

    type_provider = models.CharField(max_length=256, choices=TYPE_PROVIDERS)
    uuid_provider = models.CharField(max_length=256)
    last_name_provider = models.CharField(max_length=256)
    previous_name_provider = models.CharField(max_length=256, blank=True, null=True)

    def __str__(self):
        return f"<PlayerInfoProvider: {self.type_provider} - {self.last_name_provider}>"
