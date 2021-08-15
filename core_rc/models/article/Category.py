from django.db import models


class Category(models.Model):
    code = models.CharField(max_length=16, primary_key=True)

    def __str__(self):
        return f"<Category: {self.code}>"
