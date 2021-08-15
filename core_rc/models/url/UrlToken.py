from django.db import models


class UrlToken(models.Model):
    def generate_token_default(self):
        return 'asdf'

    token = models.CharField(max_length=32, default=generate_token_default)
    access_name = models.CharField(max_length=32)

    def __str__(self):
        return f"<{self.access_name}>"
