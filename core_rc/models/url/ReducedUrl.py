from django.db import models


class ReducedUrl(models.Model):
    url_token = models.ForeignKey(
        'UrlToken',
        on_delete=models.CASCADE,
    )
    url = models.CharField(max_length=2048)
    shortened = models.CharField(max_length=32)

    def __str__(self):
        return f"<ReducedUrl: {self.shortened} - {self.url_token.access_name}>"
