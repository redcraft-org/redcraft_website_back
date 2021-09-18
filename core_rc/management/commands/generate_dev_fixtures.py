import os
import json
import random
import uuid
import itertools

from lorem_text import lorem
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from core_rc import models
from core_rc.management.commands.utils.ArticleFactory import ArticleFactory
from core_rc.management.commands.utils.PlayerFactory import PlayerFactory
from core_rc.management.commands.utils.DonationFactory import DonationFactory


class Command(BaseCommand):
    help = 'Generate dev fixtures.'
    path = 'core_rc/fixtures'
    name_fixture = 'dev_fixtures.json'

    def add_arguments(self, parser):
        parser.add_argument(
            'count_article',
            nargs='+',
            type=int,
            help='Minimum article by category',
            default=15
        )
        parser.add_argument(
            'count_player',
            nargs='+',
            type=int,
            help='Maximum article by category',
            default=40
        )
        parser.add_argument(
            'count_donation',
            nargs='+',
            type=int,
            help='Maximum article by category',
            default=40
        )
        parser.add_argument(
            'count_discount',
            nargs='+',
            type=int,
            help='Maximum article by category',
            default=40
        )

    def handle(self, *arg, **options):
        if settings.ENVIRONMENT == 'production':
            self.stdout.write('!!! THIS COMMAND IS ONLY FOR DEVLOPMENT OR TESTING !!!')

        language_list = models.Language.objects.all()
        category_list = models.Category.objects.all()

        count_article = options['count_article'][0]
        count_player = options['count_player'][0]
        count_donation = options['count_donation'][0]
        count_discount = options['count_discount'][0]

        # Generate data
        data_article = ArticleFactory().generate(count_article, language_list, category_list)
        data_player = PlayerFactory().generate(count_player)
        data_donation = DonationFactory().generate(count_donation, count_discount, data_player['data_player'])

        data = dict(data_article, **data_player, **data_donation)
        data_list = list(itertools.chain.from_iterable([item for _, item in data.items()]))

        # Create directories if doesn't exist
        if not os.path.exists(self.path):
            os.makedirs(self.path)

        path = f'{self.path}/{self.name_fixture}'

        with open(path, "w") as f:
            json.dump(data_list, f)

        self.stdout.write(
            f'Devlopement fixtures are generated in \'{path}\'!\n' +
            'Generated:\n' +
            self.__create_str_list(data)
        )

    @staticmethod
    def __create_str_list(data):
        str_list = ''
        for key, item in data.items():
            str_list += f'\t{len(item)} {key}\n'
        return str_list