import random
import time
from datetime import datetime

from lorem_text import lorem


class Utils:
    @staticmethod
    def create_date(start_datetime=datetime(2018,1,1), stop_datetime=datetime.now()):
        if type(start_datetime) == str:
            start_datetime = datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M:%SZ')

        if type(stop_datetime) == str:
            stop_datetime = datetime.strptime(stop_datetime, '%Y-%m-%dT%H:%M:%SZ')

        start_timestamp = start_datetime.timestamp()
        stop_timestamp = stop_datetime.timestamp()

        rand_timestamp = start_timestamp + random.random() * (stop_timestamp - start_timestamp)

        return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.localtime(rand_timestamp))
    
    @staticmethod
    def create_range_date(start_datetime=datetime(2018,1,1), stop_datetime=datetime.now(), start_date_name='start_date', stop_date_name='stop_date', ratio_stop_date=1):
        start_date = Utils.create_date(start_datetime=start_datetime, stop_datetime=stop_datetime)
        stop_date = Utils.create_date(start_datetime=start_date, stop_datetime=stop_datetime)

        return {
            start_date_name: start_date,
            stop_date_name: stop_date if random.random() < ratio_stop_date else None,
        }

    @staticmethod
    def create_title(language, it_article):
        return {
            'FR': f'Un super titre {it_article}',
            'EN': f'A great title {it_article}'
        }[language.short_code]
    
    @staticmethod
    def create_slug(language, it_article):
        return {
            'FR': f'un-super-titre-{it_article}',
            'EN': f'a-great-title-{it_article}'
        }[language.short_code]

    @staticmethod
    def create_text_html(title):
        text_html = f'<div>\n<h1>{title}</h1>\n'
        for i in range(random.randint(2, 4)):
            text_html += f'<p>{lorem.paragraph()}</p>\n'
        text_html += '</div>'
        return text_html
