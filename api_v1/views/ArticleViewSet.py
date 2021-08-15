import datetime
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core_rc.models import (
    LocalizedArticle,
    LocalizedCategory,
    LocalizedPost,
    Article,
    Category,
    Post,
    Language,
)

from api_v1.serializer.ArticleSerializer import ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):

    def __get_artile(self, language, article_id):
        language = Language.objects.get(short_code=language.upper())
        article = Article.objects.get(id=article_id)

        if (article.deleted_at):
            return False

        localized_articles = LocalizedArticle.objects.get(article=article.id, language=language)

        serializer = ArticleSerializer({
            'id': localized_articles.article.id,
            'title': localized_articles.title,
            'overview': localized_articles.overview,
            'text': localized_articles.text,
            'category': localized_articles.article.category.code,
            'language': language.short_code.lower(),
            'published_at': article.published_at,
        }, many=False)

        return serializer.data

    def __get_list(self, language, category, nb='all'):
        language = Language.objects.get(short_code=language.upper())

        if category:
            category = Category.objects.get(code=category)
            list_article = Article.objects.filter(
                published_at__lte=datetime.datetime.now(),
                deleted_at=None,
                category=category.code
            ).order_by('-published_at')
        else:
            list_article = Article.objects.filter(
                published_at__lte=datetime.datetime.now(),
                deleted_at=None
            ).order_by('-published_at')

        if nb != 'all':
            list_article = list_article[:nb]

        data = []
        for article in list_article:
            localized_article = LocalizedArticle.objects.get(language=language, article=article)
            data += [{
                'id': article.id,
                'title': localized_article.title,
                'overview': localized_article.overview,
                'category': localized_article.article.category.code,
                'language': language.short_code.lower(),
                'published_at': article.published_at,
            }]

        serializer = ArticleSerializer(data, many=True)
        return serializer.data

    def retrieve(self, request, language, pk=None):
        resp = self.__get_artile(
            language=language,
            article_id=pk
        )
        if resp:
            return Response(resp)
        return Response(status=404)

    def list(self, request, language):
        return Response(self.__get_list(
            language=language,
            category=request.GET.get('category', None)
        ))

    @action(detail=False)
    def last_article(self, request, language):
        return Response(self.__get_list(
            language=language,
            category=request.GET.get('category', None),
            nb=int(request.GET.get('nb', 5))
        ))
