import random
import uuid

from lorem_text import lorem

from core_rc.management.commands.utils.Utils import Utils


class DonationFactory:
    donation_amount_min = 100
    donation_amount_max = 5000

    def generate(self, count_donation, count_discount, data_player):
        data_discount = self.__create_discount(count_discount)
        data_donation = self.__create_donation(count_donation, data_player, data_discount)

        return {
            'data_discount': data_discount,
            'data_donation': data_donation,
        }
    
    def __create_discount(self, count_discount):
        return [{
            'model': 'core_rc.Discount',
            'pk': i,
            'fields': {
                'code': lorem.words(1),
                'bonus_modifier': random.randint(1, 10) / 10 + 1,
                'success_message': lorem.words(10),
                **Utils.create_range_date(stop_date_name='end_date', ratio_stop_date=0.8),
            }
        } for i in range(1, count_discount + 1)]

    def __create_donation(self, count_donation, data_player, data_discount):
        return [{
            'model': 'core_rc.Donation',
            'pk': str(uuid.uuid4()),
            'fields': {
                'player_id': random.choice(data_player)['pk'],
                'gifter': random.choice(data_player)['pk'] if random.random() < 0.1 else None,
                'discount': random.choice(data_discount)['pk'] if random.random() < 0.2 else None,
                'amount': random.randint(self.donation_amount_min, self.donation_amount_max),
                **self.__create_currency(),
                **Utils.create_range_date(start_date_name='donation_at', stop_date_name='refunded_at', ratio_stop_date=0.2),
                'donation_id': str(uuid.uuid4()),
                'donation_processor': 'pp',
                'message': lorem.words(random.randint(3, 25)) if random.random() < 0.8 else None,
            }
        } for i in range(count_donation)]

    @staticmethod
    def __create_currency():
        return [
            {
                'currency': 'EUR',
                'conversion_rate': 1,
            },
            {
                'currency': 'USD',
                'conversion_rate': 0.85,
            },
            {
                'currency': 'CAD',
                'conversion_rate': 0.67,
            },
            {
                'currency': 'GBP',
                'conversion_rate': 1.16,
            }
        ][random.randint(0,3)]
