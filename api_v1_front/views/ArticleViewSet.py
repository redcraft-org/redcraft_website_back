import datetime
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.urls import reverse

from core_rc.models import (
    LocalizedArticle,
    LocalizedCategory,
    LocalizedPost,
    Article,
    Category,
    Post,
    Language,
)

from api_v1_front.serializer.ArticleSerializer import ArticleSerializer, ArticleDetailSerializer


class ArticleViewSet(viewsets.ViewSet):
    def __get_querryset_list(self, language, category):
        try:
            language = Language.objects.get(short_code=language.upper())
            if category != 'all':
                category = Category.objects.get(code=category)
        except Language.DoesNotExist:
            raise Error()
        except Category.DoesNotExist:
            raise Error()
        
        querry_param = {
            'language': language,
            'article__published_at__lte': datetime.datetime.now(),
            'article__deleted_at': None,
        }

        if category != 'all':
            querry_param['article__category'] = category.code

        querryset_localized_articles = LocalizedArticle.objects.filter(**querry_param)\
            .select_related('article', 'language', 'article__category')\
            .defer('text')\
            .order_by('-article__published_at')
        
        return querryset_localized_articles

    def retrieve(self, request, language, pk):
        try:
            language = Language.objects.get(short_code=language.upper())
        except Language.DoesNotExist:
            return Response(status=404)

        article = Article.objects.get(localizedarticle__slug=pk)
        localized_article = LocalizedArticle.objects\
            .select_related('article', 'language', 'article__category')\
            .get(article=article.id, language=language)

        serializer = ArticleDetailSerializer(localized_article, many=False)
        return Response(serializer.data)

    def list(self, request, language):
        per_page = request.GET.get('per_page', 10)
        page = int(request.GET.get('page', 1))
        start = (page - 1) * per_page
        stop = start + per_page

        category = request.GET.get('category', 'all')
        try:
            querryset_localized_articles = self.__get_querryset_list(language, category)
        except:
            return Response(status=404)
            

        serializer = ArticleSerializer(querryset_localized_articles[start:stop], many=True)
        return Response({
            'current_page': page,
            'per_page': per_page,
            'links': {
                'next_page': f'{reverse("article-list", args=[language])}?per_page={per_page}&page={page}',
                'prev_page': f'{reverse("article-list", args=[language])}?per_page={per_page}&page={page}',
            },
            'articles': serializer.data
        })

    @action(detail=False)
    def last(self, request, language):
        count = request.GET.get('count', 5)

        category = request.GET.get('category', 'all')
        try:
            querryset_localized_articles = self.__get_querryset_list(language, category)
        except:
            return Response(status=404)

        serializer = ArticleSerializer(querryset_localized_articles[:count], many=True)
        return Response(serializer.data)
