import random
import uuid

from lorem_text import lorem

from core_rc.management.commands.utils.Utils import Utils


class PlayerFactory():
    player_email_ratio = 0.2
    player_info_provider_previous_name_provider_ratio = 0.8
    player_info_provider_type_discord_ratio = 0.5

    def generate(self, count_player):
        data_player = self.__create_player(count_player)
        data_player_languages = self.__create_player_languages(data_player)
        data_player_info_provider = self.__create_player_info_provider(data_player)

        return {
            'data_player': data_player,
            'data_player_languages': data_player_languages,
            'data_player_info_provider': data_player_info_provider,
        }

    def __create_player(self, count):
        return [{
            'model': 'core_rc.Player',
            'pk': str(uuid.uuid4()),
            'fields': {
                'email': f'{lorem.words(1)}@{lorem.words(1)}.com' if random.random() < self.player_email_ratio else None,
                'main_language': ['FR', 'EN'][random.randint(0, 1)],
                'created_at': Utils.create_date(),
            }
        } for i in range(count)]

    def __create_player_languages(self, data_player):
        data = [{
            'model': 'core_rc.PlayerLanguage',
            'pk': i + 1,
            'fields': {
                'player_id': data['pk'],
                'language': data['fields']['main_language'],
            }
        } for i, data in enumerate(data_player)]

        count = len(data)

        data += [{
            'model': 'core_rc.PlayerLanguage',
            'pk': i + count + 1,
            'fields': {
                'player_id': data['pk'],
                'language': {'FR': 'EN', 'EN': 'FR'}[data['fields']['main_language']],
            }
        } for i, data in enumerate(data_player) if random.random() < 0.5]

        return data

    def __create_player_info_provider(self, data_player):
        # Create Provider Minecraft (required)
        data = [{
            'model': 'core_rc.PlayerInfoProvider',
            'pk': i + 1,
            'fields': {
                'player_id': data['pk'],
                'type_provider': 'mc',
                'uuid_provider': str(uuid.uuid4()),
                'last_name_provider': lorem.words(1),
                'previous_name_provider': lorem.words(1) if random.random() < self.player_info_provider_previous_name_provider_ratio else None,
            }
        } for i, data in enumerate(data_player)]

        # Create Provider Discord (optional)
        count_player_provider_mc = len(data)
        data += [{
            'model': 'core_rc.PlayerInfoProvider',
            'pk': i + 1 + count_player_provider_mc,
            'fields': {
                'player_id': data['pk'],
                'type_provider': 'di',
                'uuid_provider': str(uuid.uuid4()),
                'last_name_provider': lorem.words(1),
                'previous_name_provider': lorem.words(1) if random.random() < self.player_info_provider_previous_name_provider_ratio else None,
            }
        } for i, data in enumerate(data_player) if random.random() < self.player_info_provider_type_discord_ratio]

        return data
