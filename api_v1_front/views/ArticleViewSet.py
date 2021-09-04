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

from api_v1_front.serializer.ArticleSerializer import ArticleSerializer


class ArticleViewSet(viewsets.ViewSet):

    def __get_article(self, language, article_id):
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
            'slug': localized_articles.slug
        }, many=False)

        return serializer.data

    def __get_list(self, language, category, start, stop):
        querry_param = {
            'published_at__lte': datetime.datetime.now(),
            'deleted_at': None,
        }
        if category != 'all':
            querry_param['category'] = category.code

        list_article = Article.objects.filter(**querry_param).order_by('-published_at')[start:stop]

        data = []
        for article in list_article:
            localized_article = LocalizedArticle.objects.get(language=language, article=article)
            data += [{
                'id': article.id,
                'title': localized_article.title,
                'overview': localized_article.overview,
                'category': localized_article.article.category.code,
                'language': language.short_code.lower(),
                'slug': localized_article.slug,
                'published_at': article.published_at,
            }]

        serializer = ArticleSerializer(data, many=True)
        return serializer.data

    # Action
    def retrieve(self, request, language, pk=None):
        resp = self.__get_article(
            language=language,
            article_id=pk
        )
        if resp:
            return Response(resp)
        return Response(status=404)

    def list(self, request, language):
        per_page = request.GET.get('per_page', 10)
        page = request.GET.get('page', 1) - 1
        start = page * per_page
        stop = start + per_page

        try:
            language = Language.objects.get(short_code=language.upper())
            category = request.GET.get('category', 'all')
            if category != 'all':
                category = Category.objects.get()
        except Language.DoesNotExist:
            return Response({'error': ''}, 404)
        except Category.DoesNotExist:
            return Response({'error': ''}, 404)

        return Response(self.__get_list(language, category, start, stop))

    @action(detail=False)
    def last(self, request, language):
        return Response(self.__get_list(
            language=language,
            category=request.GET.get('category', None),
            nb=int(request.GET.get('nb', 5))
        ))
