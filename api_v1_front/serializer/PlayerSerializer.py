from django.urls import reverse
from rest_framework import serializers

from core_rc import models


class PlayerSerializer(serializers.Serializer):
    class PlayerInfoProviderSerializer(serializers.Serializer):
        last_username = serializers.CharField(source='last_name_provider')
        previous_username = serializers.CharField(source='previous_name_provider')
        provider_type = serializers.CharField(source='type_provider')


    class PlayerLanguageListSerializer(serializers.Serializer):
        code = serializers.CharField(source='language.code')
        name = serializers.CharField(source='language.name')


    id = serializers.SerializerMethodField()
    main_language = serializers.SerializerMethodField()
    languages = PlayerLanguageListSerializer(many=True)
    info = PlayerInfoProviderSerializer(many=True)
    links = serializers.SerializerMethodField()

    def get_id(self, obj):
        return f'player:{obj.id}'

    def get_main_language(self, obj):
        l = ''
        for player_language in obj.languages.all():
            if player_language.main_language:
                l = player_language.language.code
                break
        return l

    def get_links(self, obj):
        return {
            'player': self.context['request'].build_absolute_uri(reverse("player-detail", args=[obj.id]))
        }
