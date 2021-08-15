from django.db import models


class Language(models.Model):
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

    short_code = models.CharField(max_length=5, choices=LANGUAGE_CODE, primary_key=True)

    def get_name(self):
        return self.LANGUAGE_CODE[self.short_code]

    def __str__(self):
        return f"<Language: {self.short_code} - {self.name}>"
