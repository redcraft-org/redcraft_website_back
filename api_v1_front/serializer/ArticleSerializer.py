from rest_framework import serializers

from core_rc import models


class ArticleSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    overview = serializers.CharField()
    text = serializers.CharField(required=False)
    category = serializers.CharField()
    language = serializers.CharField()
    published_at = serializers.DateTimeField()
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        return {
            'article': f'127.0.0.1:8000/api/v1/{obj["language"]}/article/{obj["id"]}/{obj["slug"]}'
        }
