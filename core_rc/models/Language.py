from django.db import models


class Language(models.Model):
    code = models.CharField(max_length=5, primary_key=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"<Language: {self.short_code} - {self.name}>"
