from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from core_rc.models.url.ShortUrl import ShortUrl


def short_url(request, shortened):
    try:
        query_url = ShortUrl.objects.get(shortened__exact=shortened)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)

    return redirect(query_url.url)
