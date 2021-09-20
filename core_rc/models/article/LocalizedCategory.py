from django.db import models


class LocalizedCategory(models.Model):
    name = models.CharField(max_length=32)
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='localized_category'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(name='localized_category_unique', fields=['language', 'category']),
        ]

    def __str__(self):
        return f"<LocalizedCategory: {self.language.code} - {self.category.code}>"
