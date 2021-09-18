from django.db import models


class Coupon(models.Models):
    coupon = models.ForeignKey(
        'CouponGift',
        related_name='coupon',
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=256)
    success_message = models.TextField()
    broadcast_message = models.TextField(blank=True, null=True)

    meta_description = models.TextField(blank=True, null=True)

    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
