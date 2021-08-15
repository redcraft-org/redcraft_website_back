from django.shortcuts import redirect
from django.core.exceptions import ObjectDoesNotExist

from core_rc.models.url.ReducedUrl import ReducedUrl


def short_url(request, shortened, *args, **kwargs):
    try:
        query_url = ReducedUrl.objects.get(shortened__exact=shortened)
    except ObjectDoesNotExist:
        return redirect('home')

    return redirect(query_url.url)
