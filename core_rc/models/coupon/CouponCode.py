from django.db import models


class CouponCode(models):
    code = models.CharField(max_length=256)

    coupon = models.ForeignKey(
        'Coupon',
        related_name='code',
        on_delete=models.CASCADE
    )

    player = models.ForeignKey(
        'Player',
        related_name='coupon',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    claimed_at = models.DateTimeField()
