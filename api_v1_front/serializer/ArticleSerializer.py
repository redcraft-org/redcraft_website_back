from django.urls import reverse
from rest_framework import serializers

from core_rc import models


class ArticleSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    title = serializers.CharField()
    overview = serializers.CharField()
    translation_source = serializers.CharField()
    author = serializers.CharField()
    category = serializers.CharField(source='article.category.code')
    language = serializers.CharField(source='language.short_code')
    published_at = serializers.DateTimeField(source='article.published_at')
    links = serializers.SerializerMethodField()

    def get_links(self, obj):
        return {
            'article': self.context['request'].build_absolute_uri(reverse("article-detail", args=[obj.language.short_code, obj.slug]))
        }

    def get_id(self, obj):
        return f'article:{obj.article_id}'


class ArticleDetailSerializer(ArticleSerializer):
    text = serializers.CharField()
