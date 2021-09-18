from django.db import models
import uuid


class Discount(models.Model):
    code = models.CharField(max_length=256)
    bonus_modifier = models.FloatField()
    success_message = models.TextField()

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
