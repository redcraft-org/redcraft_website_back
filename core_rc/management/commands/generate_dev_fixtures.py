import os
import json
import random

from lorem_text import lorem

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from core_rc import models



class Command(BaseCommand):
    help = 'Generate dev fixtures.'

    def add_arguments(self, parser):
        parser.add_argument(
            'min_article',
            nargs='+',
            type=int,
            help='Minimum article by category',
            default=15
        )
        parser.add_argument(
            'max_article',
            nargs='+',
            type=int,
            help='Maximum article by category',
            default=40
        )
    
    def create_date(self):
        year = random.randint(18, 22)
        mounth  = random.randint(1,12)
        day = random.randint(1, 27)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)

        mounth = f'0{mounth}' if mounth < 10 else str(mounth)
        day = f'0{day}' if day < 10 else str(day)
        hours = f'0{hours}' if hours < 10 else str(hours)
        minutes = f'0{minutes}' if minutes < 10 else str(minutes)

        return f"20{year}-{mounth}-{day} {hours}:{minutes}Z"

    def handle(self, *arg, **options):
        if settings.ENVIRONMENT == 'prod':
            self.stdout.write('!!! THIS COMMANDE IS ONLY FOR DEVLOPMENT OR TESTING !!!')

        language_list = models.Language.objects.all()
        category_list = models.Category.objects.all()

        min_article = options['min_article'][0]
        max_article = options['max_article'][0]

        data = []

        pk_article = 1
        pk_localized_article = 1

        for category in category_list:
            for i in range(random.randint(min_article, max_article)):
                data += [{
                    'model': 'core_rc.Article',
                    'pk': pk_article,
                    'fields': {
                        'category_id': category.code,
                        'published_at': self.create_date(),
                        'deleted_at': self.create_date() if random.random() < 0.1 else None
                    }
                }]

                for language in language_list:
                    data += [{
                        'model': 'core_rc.LocalizedArticle',
                        'pk': pk_localized_article,
                        'fields': {
                            'language': language.short_code,
                            'article': pk_article,
                            'title': f'Un super titre {pk_article}',
                            'overview': lorem.words(10),
                            'text': lorem.paragraph(),
                            'slug': f'un-super-slug-{pk_article}',
                            'created_at': self.create_date(),
                            'modified_at': self.create_date(),
                        }
                    }]
                    pk_localized_article += 1

                pk_article += 1

        data_json = json.dumps(data)
        os.remove("core_rc/fixtures/dev_fixtures.json")

        f = open("core_rc/fixtures/dev_fixtures.json", "a")
        f.write(data_json)
        f.close()

        self.stdout.write(f'Devlopement fixtures is generate in {0}!')

        # self.stdout.write('Watch static...')
        # self.stdout.write('Watching :')

        # sass_handler = sassHandler()
        # observer = Observer()
        # for path_in, path_out in settings.SASS_FILES:
        #     try:
        #         compile_sass(
        #             inpath=path_in,
        #             outpath=path_out,
        #             output_style='expanded',
        #             precision=8,
        #             source_map=False
        #         ) 
        #         self.stdout.write(f'compile sass: {path_in} -> {path_out}')
        #     except sass.CompileError as exc:
        #         self.stdout.write(str(exc))

        #     observer.schedule(sass_handler, path_in, recursive=True)

        # observer.start()
        # try:
        #     while observer.is_alive():
        #         observer.join(1)
        # except KeyboardInterrupt:
        #     observer.stop()
        # self.stdout.write('Bye!')
