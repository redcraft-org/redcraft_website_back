import datetime
from math import ceil

from django.urls import reverse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from core_rc.models import (
    LocalizedArticle,
    Article,
    Category,
    Language,
)

from api_v1_front.serializer.ArticleSerializer import ArticleSerializer, ArticleDetailSerializer


class ArticleViewSet(viewsets.ViewSet):
    def __get_querryset_list(self, language, category):
        try:
            language = Language.objects.get(code=language.upper())
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
            language = Language.objects.get(code=language.upper())
        except Language.DoesNotExist:
            return Response(status=404)

        article = Article.objects.get(localizedarticle__slug=pk)
        localized_article = LocalizedArticle.objects\
            .select_related('article', 'language', 'article__category')\
            .get(article=article.id, language=language)

        serializer = ArticleDetailSerializer(
            localized_article,
            many=False,
            context={'request': request}
        )
        return Response(serializer.data)

    def list(self, request, language):
        per_page = int(request.GET.get('per_page', 10))
        page = int(request.GET.get('page', 1))

        if page < 1:
            return Response(status=404)

        start = (page - 1) * per_page
        stop = start + per_page

        category = request.GET.get('category', 'all')
        try:
            querryset_localized_articles = self.__get_querryset_list(language, category)
        except:
            return Response(status=404)
            

        serializer = ArticleSerializer(
            querryset_localized_articles[start:stop],
            many=True,
            context={'request': request}
        )

        count_article = Article.objects.filter(
            published_at__lte=datetime.datetime.now(),
            deleted_at=None
        ).count()

        url = request.build_absolute_uri(reverse("article-list", args=[language]))
        count_page = ceil(count_article / per_page)

        return Response({
            'current_page': page,
            'per_page': per_page,
            'links': {
                'prev_page': f'{url}?per_page={per_page}&page={page-1}' if page > 1 else None,
                'next_page': f'{url}?per_page={per_page}&page={page+1}' if page < count_page else None,
            },
            'list': serializer.data
        })

    @action(detail=False)
    def last(self, request, language):
        count = int(request.GET.get('count', 5))

        category = request.GET.get('category', 'all')
        try:
            querryset_localized_articles = self.__get_querryset_list(language, category)
        except:
            return Response(status=404)

        serializer = ArticleSerializer(
            querryset_localized_articles[:count],
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)
