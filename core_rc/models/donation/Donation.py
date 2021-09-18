from django.db import models
import uuid


class Donation(models.Model):
    DONATION_PROCESSORS = (
        ('pp', 'paypal'),
    )

    PROVIDER_PROCESSORS = (
        ('mc', 'minecraft'),
        ('ds', 'discord'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    player = models.ForeignKey(
        'Player',
        related_name='donations',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    gifter = models.ForeignKey(
        'Player',
        related_name='donation_gifts',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    discount = models.ForeignKey(
        'Discount',
        related_name='donation',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    amount = models.IntegerField(help_text='value in cents')
    currency = models.CharField(max_length=256, default='EUR')
    conversion_rate = models.FloatField(default=1)

    message = models.CharField(max_length=280, blank=True, null=True)

    donation_at = models.DateTimeField(auto_now_add=True)
    refunded_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    donation_id = models.CharField(max_length=256)
    donation_processor = models.CharField(max_length=2, choices=DONATION_PROCESSORS)
