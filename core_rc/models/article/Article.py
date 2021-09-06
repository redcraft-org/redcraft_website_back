from django.db import models
import uuid


class Article(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    published_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"<Article: {self.id} - {self.category.code}>"
 