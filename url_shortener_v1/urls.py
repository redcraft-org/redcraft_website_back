from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from url_shortener_v1 import views


urlpatterns = [
    path('<str:shortened>', views.short_url, name='short_url'),
]
