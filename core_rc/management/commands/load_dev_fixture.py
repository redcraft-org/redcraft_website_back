import os
import json
import random
import uuid
from lorem_text import lorem

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from core_rc import models


class Command(BaseCommand):
    help = 'Load dev fixtures.'
    path = "core_rc/fixtures/dev_fixtures.json"

    def handle(self, *arg, **options):
        if settings.ENVIRONMENT == 'production':
            self.stdout.write('!!! THIS COMMAND IS ONLY FOR DEVLOPMENT OR TESTING !!!')

        # Purge table with fixture
        models.LocalizedArticle.objects.all().delete()
        models.Article.objects.all().delete()

        # Create Load fixture
        call_command('loaddata', 'dev_fixtures.json')