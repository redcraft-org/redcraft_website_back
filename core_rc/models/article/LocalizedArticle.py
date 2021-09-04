from django.db import models


class LocalizedArticle(models.Model):
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE
    )
    article = models.ForeignKey(
        'Article',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=42)
    overview = models.CharField(max_length=255, blank=True, null=True)
    text = models.TextField()
    slug = models.SlugField(max_length=42, blank=True, null=True)

    translation_source = models.CharField(max_length=255, default='None')
    author = models.CharField(max_length=255, default='None')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(name='localized_article_unique', fields=['language', 'article']),
        ]

    def __str__(self):
        return f"<LocalizedArticle: {self.article.id} - {self.language.short_code}>"
