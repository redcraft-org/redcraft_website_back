from django.db import models


class Donation(models.Model):
    DONATION_PROCESSORS = (
        ('pp', 'paypal'),
    )

    PROVIDER_PROCESSORS = (
        ('mc', 'minecraft'),
        ('ds', 'discord'),
    )

    player = models.ForeignKey(
        'Player',
        related_name='donations',
        on_delete=models.CASCADE
    )
    amount = models.IntegerField(help_text='value in cents')

    donation_at = models.DateTimeField(auto_now_add=True)
    refunded_at = models.DateTimeField(auto_now=True)

    donation_id = models.CharField(max_length=256)
    donation_processor = models.CharField(max_length=2, choices=DONATION_PROCESSORS)