from django.db import models


class PlayerLanguage(models.Model):
    LANGUAGE_CODE = (
        ('BG', 'Bulgarian'),
        ('CS', 'Czech'),
        ('DA', 'Danish'),
        ('DE', 'German'),
        ('EL', 'Greek'),
        ('EN', 'English'),
        ('ES', 'Spanish'),
        ('ET', 'Estonian'),
        ('FI', 'Finnish'),
        ('FR', 'French'),
        ('HU', 'Hungarian'),
        ('IT', 'Italian'),
        ('JA', 'Japanese'),
        ('LT', 'Lithuanian'),
        ('LV', 'Latvian'),
        ('NL', 'Dutch'),
        ('PL', 'Polish'),
        ('PT', 'Portuguese'),
        ('RO', 'Romanian'),
        ('RU', 'Russian'),
        ('SK', 'Slovak'),
        ('SL', 'Slovenian'),
        ('SV', 'Swedish'),
        ('ZH', 'Chinese'),
    )

    language = models.CharField(max_length=5, choices=LANGUAGE_CODE)

    @property
    def name(self):
        return dict(self.LANGUAGE_CODE)[self.language]

    player = models.ForeignKey(
        'Player',
        related_name='languages',
        on_delete=models.CASCADE
    )
