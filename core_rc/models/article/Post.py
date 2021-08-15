from django.db import models


class Post(models.Model):
    img = models.ForeignKey(
        'File',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )

    published_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"<Post: {self.id}>"
