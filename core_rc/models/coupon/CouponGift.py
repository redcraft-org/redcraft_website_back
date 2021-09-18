from django.db import models


class CouponGift(models.Models):
    name = models.CharField(max_length=256)
    cmd = models.CharField(max_length=256)
    target_server = models.CharField(max_length=256, blank=True, null=True)

    meta_description = models.TextField(blank=True, null=True)
