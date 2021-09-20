from django.db import models
import uuid


class ArticleLanguage(models.Model):
    language = models.ForeignKey(
        'Language',
        on_delete=models.CASCADE
    )
 