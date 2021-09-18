from django.urls import reverse
from rest_framework import serializers

from core_rc import models


class PlayerSerializer(serializers.Serializer):
    class PlayerInfoProviderSerializer(serializers.Serializer):
        last_username = serializers.CharField(source='last_name_provider')
        previous_username = serializers.CharField(source='previous_name_provider')
        provider_type = serializers.CharField(source='type_provider')


    class PlayerLanguageListSerializer(serializers.Serializer):
        code = serializers.CharField(source='language')
        name = serializers.CharField()


    id = serializers.SerializerMethodField()
    main_language = serializers.CharField()
    languages = PlayerLanguageListSerializer(many=True)
    info = PlayerInfoProviderSerializer(many=True)
    links = serializers.SerializerMethodField()

    def get_id(self, obj):
        return f'player:{obj.id}'

    def get_links(self, obj):
        return {
            'player': self.context['request'].build_absolute_uri(reverse("player-detail", args=[obj.id]))
        }
