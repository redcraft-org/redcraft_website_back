import io
import base64
import requests
import json
from PIL import Image


class SkinProvider:
    @staticmethod
    def __get_profile_data(ref):
        # check if uuid or username
        if len(ref) <= 16:
            # Get player id (ref is player name)
            url = 'https://api.mojang.com/users/profiles/minecraft/' + ref
            response = requests.get(url)
            ref = response.json()['id']

        # Get player profile (ref is player uuid)
        url = 'https://sessionserver.mojang.com/session/minecraft/profile/' + ref
        response = requests.get(url)
        profile_data = response.json()['properties'][0]['value']
        profile_data = base64.b64decode(profile_data)
        return json.loads(profile_data)

    @staticmethod
    def __get_url_texture(profile_data):
        return profile_data['textures']['SKIN']['url']

    @staticmethod
    def __get_is_slim(profile_data):
        return 'metadata' in profile_data['textures']['SKIN']

    @staticmethod
    def __get_template_by_url(url_texture):
        response = requests.get(url_texture)
        image_bytes = io.BytesIO(response.content)
        return Image.open(image_bytes)

    @staticmethod
    def get_data(ref):
        profile_data = SkinProvider.__get_profile_data(ref)
        url_texture = SkinProvider.__get_url_texture(profile_data)
        is_slim = SkinProvider.__get_is_slim(profile_data)
        img_template = SkinProvider.__get_template_by_url(url_texture)
        return (img_template, is_slim)
