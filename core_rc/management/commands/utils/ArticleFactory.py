import random
import uuid
import datetime

from lorem_text import lorem

from core_rc.management.commands.utils.Utils import Utils


class ArticleFactory:
    article_deleted_ratio = 0.2

    def generate(self, count_article, language_list, category_list):
        data_articles = self.__create_article(category_list, count_article)
        data_localized_articles = self.__create_localized_article(data_articles, language_list)
        return {
            'data_articles': data_articles,
            'data_localized_articles': data_localized_articles
        }

    def __create_article(self, category_list, count):
        return [{
            'model': 'core_rc.Article',
            'pk': str(uuid.uuid4()),
            'fields': {
                'category_id': category.code,
                'published_at': Utils.create_date(stop_datetime=datetime.datetime.now() + datetime.timedelta(days=100)),
                'deleted_at': Utils.create_date() if random.random() < self.article_deleted_ratio else None
            }
        } for i in range(count) for category in category_list]
    
    def __create_localized_article(self, data_articles, language_list):
        data = []
        pk_localized_article = 1
        it_article = 0
        for data_article in data_articles:
            for language in language_list:
                title = Utils.create_title(language, it_article)
                created_at = Utils.create_date()
                modified_at = Utils.create_date(start_datetime=created_at)
                data += [{
                    'model': 'core_rc.LocalizedArticle',
                    'pk': pk_localized_article,
                    'fields': {
                        'language': language.short_code,
                        'article': data_article['pk'],
                        'title': title,
                        'overview': lorem.words(10),
                        'text': Utils.create_text_html(title),
                        'slug': Utils.create_slug(language, it_article),
                        'created_at': created_at,
                        'modified_at': modified_at,
                    }
                }]
                pk_localized_article += 1
            it_article += 1
        return data
