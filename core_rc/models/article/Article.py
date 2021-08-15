from django.db import models


class Article(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )

    published_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"<Article: {self.id} - {self.category.code}>"
