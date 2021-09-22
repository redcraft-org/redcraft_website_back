from django.urls import reverse
from rest_framework import serializers

from core_rc import models
from api_v1_public.serializer.PlayerSerializer import PlayerSerializer


class DonationSerializer(serializers.Serializer):
    class DiscountSerializer(serializers.Serializer):
        bonus_modifier = serializers.FloatField()
        success_message = serializers.CharField()
        start_date = serializers.DateTimeField()
        end_date = serializers.DateTimeField()

    id = serializers.CharField()
    amount = serializers.IntegerField()
    currency = serializers.CharField()
    conversion_rate = serializers.FloatField()
    message = serializers.CharField()
    donation_at = serializers.DateTimeField()
    refunded_at = serializers.DateTimeField()
    discount = DiscountSerializer()
    player = PlayerSerializer()
    gifter = PlayerSerializer()
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        return {
            'donation': self.context['request'].build_absolute_uri(reverse("donation-detail", args=[obj.id]))
        }
