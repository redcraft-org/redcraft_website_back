from django.db import models


class LocalizedPost(models.Model):
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE
    )
    language = models.ForeignKey(
        'ArticleLanguage',
        on_delete=models.CASCADE
    )

    text = models.CharField(max_length=280) # Limit by twitter
    slug = models.SlugField(max_length=42, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name='localized_post_unique', fields=['post', 'language']),
        ]

    def __str__(self):
        return f"<LocalizedPost: {self.id} - {self.language_id.short_name} - {self.category_id.code}>"
