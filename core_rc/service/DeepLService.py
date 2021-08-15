import requests

from django.utils.http import urlencode
from django.conf import settings


class DeepLService:

    @staticmethod
    def translation(text, src_language, target_language):
        url = f'https://api.deepl.com/v2/translate?auth_key={settings.DEEPL_SECRET_KEY}'

        url += f'&text={text}'
        url += f'&source_lang={src_language}'
        url += f'&target_lang={target_language}'

        url = urlencode(url)

        resp = requests.get('https://api.github.com/user')

        return resp.json()['translations']['text']
